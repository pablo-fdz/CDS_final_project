import pandas as pd
from .transformation import Transformation

class Imputer(Transformation):
    def __init__(self):
        pass

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
<<<<<<< HEAD
            '''
            Fills the nan with the mean based on the Album Name. Has to be done before column_dropper.
            '''
            self.group_by_column = 'Album Name'
            self.album_mean = self.df.groupby(self.group_by_column)[self.column_to_fill].mean()
            
            self.album_mean = self.album_mean.round(2)
            transformed_data[mean_columns] = self.df[self.mean_columns].fillna(self.df[self.group_by_column].map(self.album_mean))
            
            return transformed_data        
=======
        print('Method not implemented yet.')
        return data
>>>>>>> 585ca228e46bbf04c22a732039dc9b49caf9e343
