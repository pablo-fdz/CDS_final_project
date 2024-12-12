import pandas as pd
from .transformation import Transformation

class IntegerTransformer(Transformation):
    def __init__(self):
        self.column_types = {}

    def fit(self, data: pd.DataFrame) -> None:
        """
        Identifies columns that can be converted to integers without errors.
        """
        for column in data.columns:
            try:
                data[column].astype(int)
                self.column_types[column] = 'int'
            except (ValueError, TypeError):
                self.column_types[column] = 'drop'

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Transforms columns into integer format and drops non-convertible columns.
        Assumes `fit` has been called beforehand.
        """
        transformed_data = data.copy()
        for column, col_type in self.column_types.items():
            if col_type == 'int':
                transformed_data[column] = transformed_data[column].astype(int)
            elif col_type == 'drop':
                transformed_data.drop(columns=[column], inplace=True)
        return transformed_data