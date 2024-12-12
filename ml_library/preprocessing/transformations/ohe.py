import pandas as pd
from .transformation import Transformation

class OHE(Transformation):
    def __init__(self):
        pass

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        print('Method not implemented yet.')
        return data