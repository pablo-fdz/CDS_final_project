import pandas as pd
from .transformation import Transformation
from sklearn.impute import SimpleImputer
import numpy as np

class Imputer(Transformation):
    def __init__(self, columns: list[str] = None, strategy: str = 'mean'):
        """
        Initialize the Imputer with specified columns and imputation strategy.

        Args:
            columns (list[str], optional): List of column names to apply the imputation. Defaults to None (which applies imputation to all numerical columns).
            strategy (str, optional): Imputation strategy ('mean', 'median', 'most_frequent', or 'constant'). Defaults to 'mean'.
        """
        self.columns = columns
        self.imputer = SimpleImputer(missing_values = np.nan, strategy = strategy)

    def fit(self, data: pd.DataFrame) -> pd.DataFrame:
        if self.columns is None:
            self.columns = data.select_dtypes(include='number').columns.tolist()
        self.imputer.fit(data[self.columns])

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        data[self.columns] = self.imputer.transform(data[self.columns])
        return data