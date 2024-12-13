import pandas as pd
import unittest
import numpy as np
from preprocessing.transformations.imputer import Imputer

class TestImputer(unittest.TestCase):
    
    def setUp(self):
        # SAMPLE DATAFRAME
        self.data = pd.DataFrame({
            'A': [1, 2, np.nan, 3],
            'B': [np.nan, 5, 6, 7],
            'C': ['cat', 'dog', 'mouse', None]
        })
        # EXPECTED RESULTS
        self.expected_imputed_mean = pd.DataFrame({
            'A': [1, 2, 2, 3],  # mean of [1, 2, 4]
            'B': [6.0, 5.0, 6.0, 7.0],  # mean of [5, 6, 7]
            'C': ['cat', 'dog', 'mouse', None]  # should remain untouched
        })

    def test_imputer_fit_transform(self):
        # Test the Imputer with mean strategy for specific columns
        imputer = Imputer(columns=['A', 'B'], strategy='mean')
        
        imputer.fit(self.data)
        transformed_data = imputer.transform(self.data.copy())
        
        # TESTING MEANS ARE CORRECT
        pd.testing.assert_frame_equal(
            transformed_data[['A', 'B']], 
            self.expected_imputed_mean[['A', 'B']],
            check_exact=False  # Allow for floating-point precision differences
        )
        
        # TESTING THAT NON-NUMERIC COLUMNS REMAIN THE SAME
        self.assertTrue(
            all(transformed_data['C'] == self.data['C']),
            "Non-numeric columns should remain unchanged."
        )

    def test_imputer_fit_all_numeric(self):
        # TESTING THAT THE IMPUTER SELECTS THE COLUMNS CORRECTLY
        imputer = Imputer(strategy='mean')
        
        imputer.fit(self.data)
        transformed_data = imputer.transform(self.data.copy())
        
        # RESULTS SHOULD BE THE SAME AS BEFORE
        pd.testing.assert_frame_equal(
            transformed_data[['A', 'B']], 
            self.expected_imputed_mean[['A', 'B']],
            check_exact=False
        )
        
        self.assertTrue(
            all(transformed_data['C'] == self.data['C']),
            "Non-numeric columns should remain unchanged."
        )

if __name__ == "__main__":
    unittest.main()
