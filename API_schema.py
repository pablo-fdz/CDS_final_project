from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List, Optional
import ml_library as ml

#directory model
MODEL_DIR= "data/model.pkl"

#instantiate FastAPI
app = FastAPI()

# Define input data schema with explicit columns matching the JSON structure
class InputDataFrame(BaseModel):
    Track: List[Optional[str]]
    Album_Name: List[Optional[str]]
    Artist: List[Optional[str]]
    Release_Date: List[Optional[str]]
    ISRC: List[Optional[str]]
    All_Time_Rank: List[Optional[str]]
    Track_Score: List[Optional[float]]
    Spotify_Streams: List[Optional[str]]
    Spotify_Playlist_Count: List[Optional[str]]
    Spotify_Playlist_Reach: List[Optional[str]]
    Spotify_Popularity: List[Optional[str]]
    YouTube_Views: List[Optional[str]]
    YouTube_Likes: List[Optional[str]]
    TikTok_Posts: List[Optional[str]]
    TikTok_Likes: List[Optional[str]]
    TikTok_Views: List[Optional[str]]
    YouTube_Playlist_Reach: List[Optional[str]]
    Apple_Music_Playlist_Count: List[Optional[str]]
    AirPlay_Spins: List[Optional[str]]
    SiriusXM_Spins: List[Optional[str]]
    Deezer_Playlist_Count: List[Optional[str]]
    Deezer_Playlist_Reach: List[Optional[str]]
    Amazon_Playlist_Count: List[Optional[str]]
    Pandora_Streams: List[Optional[str]]
    Pandora_Track_Stations: List[Optional[str]]
    Soundcloud_Streams: List[Optional[str]]
    Shazam_Counts: List[Optional[str]]
    TIDAL_Popularity: List[Optional[str]]


@app.post("/predict")
async def predict(data: InputDataFrame):
    # Load model, and cnvert input data to a DataFrame with columns oriented correctly
    try:
        model = joblib.load(MODEL_DIR)
        
        df = pd.DataFrame.from_dict(data.dict(), orient="columns")
        print("DataFrame for prediction:\n")  
        df.columns = df.columns.str.replace('_', ' ')

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error converting input data to DataFrame: {e}")

    # Check if DataFrame has the correct shape
    if df.shape[1] != 28:
        raise HTTPException(status_code=400, detail="Invalid number of features in the dataframe")

    # Make predictions
    try:
        predictions = model.predict(df)
        table = pd.DataFrame({
        "Song": df['Track'],
        "Category": ["Explicit" if val == 1 else "Clean" for val in predictions]
         })

        print(table)

        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")

    #return predictions.tolist()
    return table