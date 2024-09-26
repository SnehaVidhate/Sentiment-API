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

# # Configure logging
# logging.basicConfig(level=logging.INFO)

def get_sentiment(review_text):
    for _ in range(3):  
        # Retry up to 3 times

            # Prepare the prompt
            prompt = f"""
            You are a sentiment analysis model. Analyze the sentiment of the following text and return a JSON object with positive, negative, and neutral scores that sum to 1.0. Text: "{review_text}"
            OUTPUT:
            {{"positive": 0.8, "negative": 0.1, "neutral": 0.1}}
           
            
            ---
            **Note**: Do not provide extra unnecessary information in the output other expected JSON object.
            
            """

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
            time.sleep(1)  # Wait a second before retrying
            
            return response_content


l = ['Great product, very useful!', 'Poor quality and bad customer service.😡', 'Exceeded my expectations, fantastic!', 'Terrible, not worth the money.😞', 'Quite good, but could be improved.', 'Mediocre at best, not recommended.', 'Wonderful design, highly recommended!', 'Awful experience, would not buy again.', 'Solid product, good value for the price.', 'Highly satisfied with the purchase.', 'The product broke after a few uses.', 'I would definitely buy this again!😄', 'Not as described, very disappointed.', 'Customer service was really helpful.', 'It works perfectly as expected.', 'I had a terrible experience with this.', 'Well worth the money.', 'Waste of time and money.', 'Absolutely love this product!', 'It didn’t work as advertised.', 'Very reliable and easy to use.', 'I had higher expectations, sadly disappointed.', 'Delivered quickly, works as intended.', 'Horrible quality, won’t buy again.', 'This is the best purchase I’ve made.', 'It stopped working after a month.', 'I’m quite pleased with this product.', 'Very cheap material, not durable.', 'Fantastic performance for the price.', 'Extremely frustrating experience.', 'User-friendly and well-designed.', 'Not worth the price at all.🙁', 'Better than expected!', 'The instructions were very unclear.', 'Would definitely recommend to others.', 'Very underwhelming experience.', 'Does the job, no complaints.', 'I regret purchasing this item.', 'Great value for money!😃', 'Arrived damaged, very disappointed.', 'Exceeded my expectations!', 'Not what I was hoping for.', 'Happy with the purchase overall.', 'Total waste of money.', 'Amazing product, highly satisfied!', 'Not durable, broke after a few uses.', 'Fantastic design and great quality.', 'Wouldn’t recommend to others.', 'Excellent value, would buy again.', 'Terrible product, avoid at all costs.']
count =0 
for i in l:
    print(get_sentiment(i) , count)
    count +=1
    print('-------------------')