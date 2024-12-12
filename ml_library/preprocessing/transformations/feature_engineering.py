

import pandas as pd
from .transformation import Transformation

class FeatureEngineering(Transformation):
    def fit(self, data: pd.DataFrame) -> None:
        """
        No fitting required for feature engineering.
        """
        pass

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Applies feature engineering steps to the dataset.
        """
        transformed_data = data.copy()
        transformed_data = self.create_features(transformed_data)
        return transformed_data

    def create_features(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Creates additional features based on existing data.
        """
        data['log_spotify_streams'] = np.log1p(data['Spotify Streams'])
        data['log_pandora_streams'] = np.log1p(data['Pandora Streams'])
        data['total_playlist_count'] = (
            data['Spotify Playlist Count'] + 
            data['Deezer Playlist Count'] + 
            data['Amazon Playlist Count']
        )
        data['playlist_reach_ratio'] = data['Spotify Playlist Reach'] / (data['Spotify Streams'] + 1)
        #data['release_year'] = pd.to_datetime(data['Release Date'], errors='coerce').dt.year
        return data