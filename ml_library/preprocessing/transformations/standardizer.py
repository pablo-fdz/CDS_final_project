import pandas as pd
from .transformation import Transformation
from sklearn.preprocessing import StandardScaler

class Standardizer(Transformation):
    def __init__(self, columns: list[str] = None):
        self.columns = columns
        self.scaler = StandardScaler()

    def fit(self, data: pd.DataFrame) -> pd.DataFrame:
        if self.columns is None:
            self.columns = data.select_dtypes(include='number').columns.tolist()
        self.scaler.fit(data[self.columns])

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        data[self.columns] = self.scaler.transform(data[self.columns])
        return data