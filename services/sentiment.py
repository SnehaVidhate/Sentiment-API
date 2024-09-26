import os
import json
import logging
import time
from groq import Groq
from fastapi import HTTPException

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq client
client = Groq()

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_sentiment(review_text):
    for _ in range(3):  
        # Retry up to 3 times
        try:
            # Prepare the prompt
            prompt = f"""Analyze the sentiment of the following text and return a JSON object with positive, negative, and neutral scores that sum to 1.0. Text: "{review_text}"

            Return only the JSON object without any additional text."""

            # Call the Groq API
            completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama3-groq-8b-8192-tool-use-preview",  # or another available model
                temperature=0,
                max_tokens=100,
            )

            # Parse the response
            response_content = completion.choices[0].message.content.strip()

            # Log the raw response content
            logging.info("Raw Response Content: %s", response_content)
            
            # Attempt to load the response as JSON
            try:
                sentiment_scores = json.loads(response_content)
                return sentiment_scores
            except json.JSONDecodeError:
                logging.error("Failed to decode JSON: %s", response_content)
                raise HTTPException(status_code=500, detail="Invalid JSON response from sentiment analysis API.")

        except Exception as e:
            logging.warning("Error: %s. Retrying...", str(e))
            time.sleep(5)  # Wait a second before retrying

    raise HTTPException(status_code=500, detail="Sentiment analysis failed after multiple attempts.")

# Function to analyze sentiment for the entire CSV and return aggregated sentiment results
def analyze_sentiment_aggregate(reviews):
    sentiments = {"positive": 0, "negative": 0, "neutral": 0}

    # Store all sentiment results
    all_sentiment_results = []

    for review in reviews:
        sentiment_result = get_sentiment(review)

        # Append each sentiment result to the list
        all_sentiment_results.append(sentiment_result)

        # Accumulate the sentiment scores
        sentiments["positive"] += sentiment_result.get("positive", 0)
        sentiments["negative"] += sentiment_result.get("negative", 0)
        sentiments["neutral"] += sentiment_result.get("neutral", 0)

    # You can log or process all_sentiment_results here if needed
    logging.info("All Sentiment Results: %s", all_sentiment_results)

    return sentiments

# Function to analyze sentiment for each individual review and return results
def analyze_sentiment_individual(reviews):
    sentiment_results = []

    # Store all sentiment results
    all_sentiment_results = []

    for review in reviews:
        sentiment_result = get_sentiment(review)

        # Append the result with the review text for clarity
        sentiment_results.append({
            "review": review,
            "sentiment": sentiment_result
        })

        # Append each sentiment result to the list
        all_sentiment_results.append(sentiment_result)

    # You can log or process all_sentiment_results here if needed
    logging.info("All Sentiment Results: %s", all_sentiment_results)

    return sentiment_results
