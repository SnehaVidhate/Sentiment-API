from fastapi import FastAPI, File, UploadFile, HTTPException
from utils.file_processing import read_reviews
from services.sentiment import analyze_sentiment_aggregate, analyze_sentiment_individual

app = FastAPI()

# Default endpoint to check if the API is running
@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running"}

# API endpoint to analyze the entire CSV and return aggregated sentiment results
@app.post("/analyze/aggregate")
async def analyze_reviews_aggregate(file: UploadFile = File(...)):
    try:
        reviews = await read_reviews(file)
        sentiments = analyze_sentiment_aggregate(reviews)
        return sentiments
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")

# API endpoint to analyze each review and return individual sentiment results
@app.post("/analyze/individual")
async def analyze_reviews_individual(file: UploadFile = File(...)):
    try:
        reviews = await read_reviews(file)
        sentiment_results = analyze_sentiment_individual(reviews)
        return sentiment_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")
