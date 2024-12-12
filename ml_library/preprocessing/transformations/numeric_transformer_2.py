import pandas as pd
from .transformation import Transformation

class Numeric_Transformer_2(Transformation):
    def __init__(self):
        self.numeric_strings = ['Spotify Playlist Count', 'Spotify Playlist Reach', 'Deezer Playlist Reach', 'All Time Rank']

    # Transform additional numeric strings into integers
    def transform_numeric_strings(data, columns):
        for col in columns:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col].str.replace(',', ''), errors='coerce')
        return data

    def fit(self, data: pd.DataFrame) -> pd.DataFrame:
        return data

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        # TODO: Ensure that fit has been called previous
        return self.transform_numeric_strings(data.copy())
