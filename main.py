from flask import Flask, render_template, request 
from PyPDF2 import PdfReader #PdfFileReader
from langchain import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS #ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os 

prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that that can answer questions about document based on the input documents.
        
        Answer the following question: {question}
        By searching the following documents: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        """,
)


raw_text=""
answer=""
texts=[]
api=""

baseDirectory=os.getcwd()

def convert2text(pdfFile):
  """Converts PDF file to texts and return the text"""
  rText=""
  name= pdfFile.filename
  filePath= os.path.join('uploads',name)
  pdfFile.save(filePath)
  reader=PdfReader(filePath)
  for i, page in enumerate(reader.pages):
      text = page.extract_text()
      if text:
          rText += text
  os.remove(filePath)
  return rText


def textSplitter(text):
  """Splits large text to chuncks"""

  text_splitter = CharacterTextSplitter(        
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
  )
  text = text_splitter.split_text(text)
  return text

def qAndA(text,api,query):
  """Given an OpenAI API key, a document and a question
  this function will return an answer"""
  embeddings = OpenAIEmbeddings(openai_api_key=api)
  docsearch = FAISS.from_texts(text, embeddings)
  chain = load_qa_chain(OpenAI(openai_api_key=api), chain_type="stuff")
  docs = docsearch.similarity_search(query)
  res=chain.run(input_documents=docs, question=query)
  return res
  


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
  global texts
  global answer
  global raw_text
  global api
  if request.method=="POST":

  # Obtain data from the form
    if ('apikey' in request.form) or ('file' in request.files):
      file = request.files['file']
      api = request.form['apikey']

  # Read the pdf document and convert it to raw text
      raw_text = convert2text(file)
  # Split the text document into chunks
      split= textSplitter(raw_text)
      texts = split
      
      

  # Searches for relevant chunk of text and use it to answer the given query
    elif ('question' in request.form) and (bool(texts)==True):
      query= request.form['question']
      answer= qAndA(texts,api,query) 
    else:
      answer= "try changing your api"
  return render_template("index.html",answer=answer)


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)