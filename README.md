# Sentiment Analysis API

A FastAPI-based application for analyzing sentiment of text reviews using the Groq API. This application processes customer reviews from a CSV file and provides sentiment analysis scores (positive, neutral, negative) for each review or aggregated results across multiple reviews. The Groq API is used to perform sentiment analysis, classifying the review text into sentiment categories based on the tone and content of the text.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/SnehaVidhate/Sentiment-API.git
   cd sentiment-api
   

2. Create and activate a virtual environment:
   bash
   python -m venv myenv
   source myenv/bin/activate   # For Linux/macOS
   # On Windows use:
   .\myenv\Scripts\Activate
   

3. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

## Project Structure


sentiment-api/
│
├── main.py                # Entry point for the FastAPI application
├── services/
│   ├── _init_.py        # Makes 'services' a Python package
│   └── sentiment.py       # Contains sentiment-related logic (Groq API interaction)
├── utils/
│   ├── _init_.py        # Makes 'utils' a Python package
│   └── file_processing.py # Contains file validation and processing logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)

## Configuration
1. Set up your Groq API key:
   - Sign up for a Groq account and obtain your API key.
   - Set your API key as an environment variable:
     bash
     export GROQ_API_KEY=your_api_key_here
     
   - For Windows, use:
     
     set GROQ_API_KEY=your_api_key_here
     

2. (Optional) Configure the Groq model:
   - Open `services/sentiment.py` and modify the `model` parameter in the `get_sentiment` function if you want to use a different Groq model.

## Running the API

To run the FastAPI server, use the following command:

bash
uvicorn main:app --reload


This will start the FastAPI server at [http://127.0.0.1:8000](http://127.0.0.1:8000). The `--reload` flag allows the server to restart automatically when changes are made to the code.

## API Endpoints

### Analyze Sentiment (Individual Reviews)

- **URL**: `/analyze/individual`
- **Method**: `POST`
- **Description**: Analyze sentiment for individual reviews in a CSV file.
- **Request Body**: Form data with a CSV file containing reviews.
- **Response**: JSON array of objects, each containing a review and its sentiment scores.

### Analyze Sentiment (Aggregate Reviews)

- **URL**: `/analyze/aggregate`
- **Method**: `POST`
- **Description**: Analyze sentiment across all reviews and return an aggregated score.
- **Request Body**: Form data with a CSV file containing reviews.
- **Response**: JSON object with aggregated sentiment scores.

## Usage Examples

### Using cURL

1. Analyze individual reviews:
   bash
   curl -X POST http://localhost:8000/analyze/individual \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/your/reviews.csv"
   

2. Analyze aggregate sentiment:
   bash
   curl -X POST http://localhost:8000/analyze/aggregate \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/your/reviews.csv"
   

### Using Python requests

python
import requests
url = "http://localhost:8000/analyze/individual"  # or /analyze/aggregate
files = {'file': open('path/to/your/reviews.csv', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```
```
