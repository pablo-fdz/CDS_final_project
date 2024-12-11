from .transformations import Transformation
import pandas as pd

class PreprocessingPipeline:
    def __init__(self, transformations: list[Transformation]):
        self.transformations = transformations
    
    def fit(self, data: pd.DataFrame) -> None:
        for transformation in self.transformations:
            transformation.fit(data)

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        data_copy = data.copy()
        for transformation in self.transformations:
            data_copy = transformation.transform(data_copy)
        return data_copy