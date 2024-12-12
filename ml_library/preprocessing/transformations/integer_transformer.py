import pandas as pd
from .transformation import Transformation

class IntegerTransformer(Transformation):
    def __init__(self):
        self.column_types = {}

    def fit(self, data: pd.DataFrame, verbose = False) -> None:
        """
        Identifies columns that contain numeric data, including those with commas, and marks them for transformation.
        """
        for column in data.columns:
            try:
                # Attempt to replace commas and convert to numeric type
                pd.to_numeric(data[column].replace({',': ''}, regex=True), errors='raise')
                self.column_types[column] = 'int'
            except (ValueError, TypeError):
                self.column_types[column] = 'drop'
        if verbose == True:
            print(self.column_types)

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Transforms numeric columns into integer format, handling commas, and drops non-convertible columns.
        Assumes `fit` has been called beforehand.
        """
        transformed_data = data.copy()
        for column, col_type in self.column_types.items():
            if col_type == 'int':
                transformed_data[column] = pd.to_numeric(
                    transformed_data[column].replace({',': ''}, regex=True), errors='coerce'
                ).fillna(0).astype(int)
            elif col_type == 'drop':
                transformed_data.drop(columns=[column], inplace=True)
        return transformed_data
