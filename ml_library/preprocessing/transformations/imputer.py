import pandas as pd
from .transformation import Transformation

class Imputer(Transformation):
    def __init__(self, group_by_column: str = 'Album Name'):
        """
        Initializes the Imputer class.
        To be applied after integer_transformer.

        Arguments: Column to group by when calculating means - 'Album Name'
        """
        self.group_by_column = group_by_column
        self.group_means = None

    def fit(self, data: pd.DataFrame) -> None:
        """
        Calculates and stores the mean of numerical columns grouped by Album Name.
        """
        self.group_means = data.groupby(self.group_by_column).mean()

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the stored means to fill NaN values in numerical columns.
        It also drops the Album Name column.
        """
        if self.group_means is None:
            raise RuntimeError("The `fit` method must be called before `transform`.")
        
        transformed_data = data.copy()
        for column in self.group_means.columns:
            if column in transformed_data.columns:
                transformed_data[column] = transformed_data[column].fillna(
                    transformed_data[self.group_by_column].map(self.group_means[column]))

        transformed_data = transformed_data.drop(columns=[self.group_by_column])
        return transformed_data
