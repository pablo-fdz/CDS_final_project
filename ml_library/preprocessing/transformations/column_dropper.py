import pandas as pd
from .transformation import Transformation

class Column_Dropper(Transformation):
    def __init__(self):
        self.columns_to_drop = ['Track', 'Album Name', 'Artist', 'ISRC', 'All Time Rank', 
                                'Track Score', 'All Time Rank', 'Spotify Playlist Count', 
                                'Spotify Playlist Reach', 'Release Date', 
                                'Apple Music Playlist Count', 'Deezer Playlist Count',
                                'Deezer Playlist Reach', 'Amazon Playlist Count', 'TIDAL Popularity'] 

    def drop_columns(self, data):
        data = data.drop(self.columns_to_drop, axis=1)