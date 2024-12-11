import pandas as pd
from .transformation import Transformation
from sklearn.preprocessing import StandardScaler

class Standardizer(Transformation):
    def __init__(self):
        self.scaler = StandardScaler()

    def fit(self, data: pd.DataFrame) -> pd.DataFrame:
        self.scaler.fit(data)

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        # TODO: Ensure that fit has been called previously
        return self.scaler.transform(data.copy())