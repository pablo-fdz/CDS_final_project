import pandas as pd
from .transformation import Transformation

class Imputer(Transformation):
    def __init__(self, mean_column, data):
            '''
            Class that perform calculations and fillings based on the mean of a column.
            
            :param mean_column: Column name where you want to perform the operations.
            :param df: Input Dataframe
            
            :return None: It directly modifies the df that you pass to the MeanOperations_ByColumn Object.
            '''
        
            self.mean_columns = data.columns
            self.data = data

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
            '''
            Fills the nan with the mean based on the Album Name. Has to be done before column_dropper.
            '''
            self.group_by_column = 'Album Name'
            self.album_mean = self.df.groupby(self.group_by_column)[self.column_to_fill].mean()
            
            self.album_mean = self.album_mean.round(2)
            self.df[self.mean_columns] = self.df[self.mean_columns].fillna(self.df[self.group_by_column].map(self.album_mean))
            
            return data        