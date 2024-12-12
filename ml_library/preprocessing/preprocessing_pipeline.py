from .transformations import Transformation
from typing import Self
import pandas as pd

class PreprocessingPipeline:
    """
    A pipeline for applying a sequence of transformations to a dataset.

    This class is designed to work seamlessly with scikit-learn workflows and supports
    chaining multiple transformations that inherit from the `Transformation` base class.
    It first fits the transformations on the input data, then applies the transformations
    in sequence.

    Attributes:
        transformations (list[Transformation]): A list of transformation objects, where each
            transformation inherits from the `Transformation` base class and defines its own
            `fit` and `transform` methods.
        is_fitted_ (bool): A flag indicating whether the pipeline has been fitted to data.

    Methods:
        fit(X: pd.DataFrame) -> Self:
            Fits each transformation in the pipeline to the input data.

        transform(X: pd.DataFrame) -> pd.DataFrame:
            Applies the fitted transformations to the input data in sequence.
    """

    def __init__(self, transformations: list[Transformation] = []):
        """
        Initializes the PreprocessingPipeline with a list of transformations.

        Args:
            transformations (list[Transformation]): A list of transformations to be applied
                sequentially. Each transformation must inherit from the `Transformation` base class.
        """
        self.transformations = transformations
        self.is_fitted_ = False

    def fit(self, X: pd.DataFrame) -> Self:
        """
        Fits each transformation in the pipeline to the data (if the transformation
        doesn't have a .fit method, it just passes).

        Args:
            X (pd.DataFrame): The input data to fit the transformations.

        Returns:
            Self: The fitted PreprocessingPipeline instance.
        """
        for transformation in self.transformations:
            transformation.fit(X)
        self.is_fitted_ = True
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Transforms the data by applying the fitted transformations in sequence.

        Args:
            X (pd.DataFrame): The input data to transform.

        Returns:
            pd.DataFrame: The transformed data.
        """
        X_copy = X.copy()
        for transformation in self.transformations:
            X_copy = transformation.transform(X_copy)
        return X_copy
