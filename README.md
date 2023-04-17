# PDF Question Answering Web Application

This is a web application that allows users to ask questions about the content of a PDF file and receive answers. The application is built using the Flask microframework,langchain library was also used to help with processing the PDF file and utilisation of the large language model.

## Features

- Upload PDF files: Users can upload PDF files to the application for processing.
- Ask Questions: Users can ask questions about the content of the uploaded PDF files using natural language queries.
- Get Answers: The application uses OpenAI GPT 3 model via API to analyze the uploaded PDF files and provide accurate answers to user questions.

## Installation

To install and run the application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python main.py`.
4. Access the application in your web browser at `http://localhost:0000`.

## Usage

To use the application, follow these steps:

1. Upload a PDF file and paste your OpenAI API key as an input in the form then use the "submit" button on the section.
2. Ask a question about the content of the uploaded PDF file using the search bar.
3. View the answer to your question on the results section.

## Demo

[Click here](https://replit.com/@Funbi/PDF-question-answering-app?s=app) to view a live demo of the application.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
