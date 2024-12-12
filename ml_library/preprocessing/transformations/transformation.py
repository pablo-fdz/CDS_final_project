from abc import ABCMeta, abstractmethod
import pandas as pd

class Transformation(metaclass = ABCMeta):
    def fit(self, data: pd.DataFrame) -> None:
        """
        Computes the transformation parameters appropriate for the data. By default,
        it doesn't do anything unless the specific transformation sets a fit method.

        E.g., computes the mean and the standard deviation of the numerical variables
        of the data.

        """
        pass

    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the data transformation.

        Assumes that the transformation has been fitted previously, if necessary.
        
        """
        return NotImplementedError