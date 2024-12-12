import pandas as pd
from .transformation import Transformation

class NanRemover(Transformation):
    def __init__(self):
        pass

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna()