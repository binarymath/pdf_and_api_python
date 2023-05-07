# 🤖 Working with api and manipulating pdf

![Imagem do rojeto](img/api_pdf.gif){ width=100% }


PDF2OpenAI is a Python-based system that receives a PDF file as input, sends a request to the OpenAI API on RapidAPI, and generates a new PDF file as output containing the response generated by OpenAI.

## 🚀 Getting Started

### Prerequisites

To use Working with api and manipulating pdf, you'll need to have the following installed on your system:

- Python 3.6 or higher
- pypdf2
- fpdf
- requests
- python-dotenv

### Installation

1. Clone the repository:

```
git clone https://github.com/your_username/pdf_and_api_python.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Set your RapidAPI key as an environment variable in `.env` file:

```
OPENAI_API_KEY=your_api_key_here
RAPIDAPI_API_KEY=your_api_key_here
```

### Usage

To run PDF2OpenAI, use the following command:

```
python pdf_processor.py
```

Make sure to put the PDF files you want to process in the `input_files` directory.

## 🤖 How it Works

PDF2OpenAI first extracts the text content from the input PDF file using pypdf2 library. It then sends this text to the OpenAI API on RapidAPI using the requests library, and retrieves the generated response. Finally, fpdf library is used to insert the response into a new PDF file, which is stored in the `output_files` directory.

## 🤝 Contributing

Contributions are welcome! To contribute to Working with api and manipulating pdf, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and write tests for them.
4. Submit a pull request.

