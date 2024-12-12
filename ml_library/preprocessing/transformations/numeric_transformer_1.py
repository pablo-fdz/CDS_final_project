import pandas as pd
from .transformation import Transformation

class Numeric_Transformer_1(Transformation):
    def __init__(self):
        self.columns_to_convert = [
            "Spotify Streams", "YouTube Views", "YouTube Likes", "TikTok Posts", "TikTok Likes",
            "TikTok Views", "YouTube Playlist Reach", "AirPlay Spins", "SiriusXM Spins", "Pandora Streams",
            "Pandora Track Stations", "Soundcloud Streams", "Shazam Counts"
        ]
    #numeric converter 
    def convert_to_numeric(column, data):
        return pd.to_numeric(data[column].str.replace(',', ''), errors='coerce') if column in data.columns else data[column]

    def fit(self, data: pd.DataFrame) -> pd.DataFrame:
        return data

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        # TODO: Ensure that fit has been called previously
        df = data.copy()


        for col in self.columns_to_convert:
            df[col] = self.convert_to_numeric(col,data)

        # Fill missing values with mean for numeric columns
        df.fillna(df.mean(numeric_only=True), inplace=True)


        return df
