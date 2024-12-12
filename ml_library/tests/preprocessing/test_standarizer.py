import pandas as pd
import unittest
import datetime
from preprocessing import Standarizer
import pytest

class TestStandardizer(unittest.TestCase):

    def setUp(self):
        # SAMPLE DATAFRAME
        self.data = pd.DataFrame({
            'A': [10, 20, 30],
            'B': [1.5, 2.5, 3.5],
            'C': ['x', 'y', 'z'] 
        })
        # EXPECTED RESULT
        self.expected_standardized = pd.DataFrame({
            'A': [-1.224744871391589, 0.0, 1.224744871391589],
            'B': [-1.224744871391589, 0.0, 1.224744871391589],
            'C': ['x', 'y', 'z']  
        })

    def test_standardizer_fit_transform(self):
        # APPLYING THE STANDARIZER TO OUR NUMERIC COLUMNS
        standardizer = Standardizer(columns=['A', 'B'])
        
        standardizer.fit(self.data)
        transformed_data = standardizer.transform(self.data.copy())
        
        #TESTING THAT NUMERIC COLUMNS ARE STANDARIZED
        pd.testing.assert_frame_equal(
            transformed_data[['A', 'B']], 
            self.expected_standardized[['A', 'B']],
            check_less_precise=True
        )

        #TESTING THAT NON-NUMERIC COLUMNS DON'T CHANGE        
        self.assertTrue(
            all(transformed_data['C'] == self.data['C']),
            "Non-numeric columns should remain unchanged."
        )

    def test_standardizer_fit_all_numeric(self):
        standardizer = Standardizer()
        
        standardizer.fit(self.data)
        transformed_data = standardizer.transform(self.data.copy())
        
        #TESTING NUMERIC COLUMNS, A AND B IN OUR SAMPLE DF ABOVE
        pd.testing.assert_frame_equal(
            transformed_data[['A', 'B']], 
            self.expected_standardized[['A', 'B']],
            check_less_precise=True
        )

        #TESTING THAT NON-NUMERIC COLUMNS DON'T CHANGE
        self.assertTrue(
            all(transformed_data['C'] == self.data['C']),
        )

if __name__ == "__main__":
    unittest.main()
