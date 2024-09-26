import pandas as pd
from io import BytesIO
from fastapi import HTTPException

async def read_reviews(file):
    # Validate file type
    if not (file.filename.endswith('.csv') or file.filename.endswith('.xlsx')):
        raise HTTPException(status_code=400, detail="Only CSV or XLSX files are supported.")

    # Read the uploaded file
    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(BytesIO(await file.read()))
        elif file.filename.endswith('.xlsx'):
            df = pd.read_excel(BytesIO(await file.read()))

        # Check for 'review' column
        if 'Review' not in df.columns:
            raise HTTPException(status_code=400, detail="Missing 'review' column in the file.")

        reviews = df['Review'].dropna().tolist()
        return reviews

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read the file: {str(e)}")
