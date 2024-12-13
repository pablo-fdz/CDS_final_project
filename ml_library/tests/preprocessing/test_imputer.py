import pandas as pd
import unittest
import numpy as np
from preprocessing.transformations.imputer import Imputer

class TestImputer(unittest.TestCase):
    
    def setUp(self):
        # Sample DataFrame
        self.data = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [np.nan, 5, 6, 7],
            'C': ['cat', 'dog', 'mouse', None]
        })
        # Expected Result after 'mean' imputation
        self.expected_imputed_mean = pd.DataFrame({
            'A': [1, 2, 2.3333333333333335, 4],  # mean of [1, 2, 4]
            'B': [6.0, 5.0, 6.0, 7.0],  # mean of [5, 6, 7]
            'C': ['cat', 'dog', 'mouse', None]  # untouched
        })

    def test_imputer_fit_transform(self):
        # Test the Imputer with mean strategy for specific columns
        imputer = Imputer(columns=['A', 'B'], strategy='mean')
        
        imputer.fit(self.data)
        transformed_data = imputer.transform(self.data.copy())
        
        # Test that numeric columns are imputed correctly
        pd.testing.assert_frame_equal(
            transformed_data[['A', 'B']], 
            self.expected_imputed_mean[['A', 'B']],
            check_exact=False  # Allow for floating-point precision differences
        )
        
        # Test that non-numeric columns remain unchanged
        self.assertTrue(
            all(transformed_data['C'] == self.data['C']),
            "Non-numeric columns should remain unchanged."
        )

    def test_imputer_fit_all_numeric(self):
        # Test the Imputer with automatic selection of numeric columns
        imputer = Imputer(strategy='mean')
        
        imputer.fit(self.data)
        transformed_data = imputer.transform(self.data.copy())
        
        # Test numeric columns are imputed correctly
        pd.testing.assert_frame_equal(
            transformed_data[['A', 'B']], 
            self.expected_imputed_mean[['A', 'B']],
            check_exact=False
        )
        
        # Test that non-numeric columns remain unchanged
        self.assertTrue(
            all(transformed_data['C'] == self.data['C']),
            "Non-numeric columns should remain unchanged."
        )

if __name__ == "__main__":
    unittest.main()
