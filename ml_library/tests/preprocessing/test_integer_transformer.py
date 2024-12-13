import unittest
import pandas as pd
from preprocessing.transformations.integer_transformer import IntegerTransformer

class TestIntegerTransformer(unittest.TestCase):

    def setUp(self):
        # SAMPLE DATA FRAME
        self.data = pd.DataFrame({
            'A': [1.1, 2.2, 3.3],   # Float column 
            'B': [10, 20, 30],      # Integer column
            'C': ['x', 'y', 'z'],   # Non-numeric column
            'D': [5, None, 15]      # Column with a missing value
        })

        self.expected_fit = {
            'A': 'int',
            'B': 'int',
            'C': 'drop',
            'D': 'int'
        }

        self.expected_transformed = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [10, 20, 30],
            'D': [5, None, 15]
        })

    # TEST FOR THE FIT FUNCTION
    def test_fit(self):
        transformer = IntegerTransformer()
        transformer.fit(self.data)

        self.assertEqual(transformer.column_types, self.expected_fit)

    # TEST FOR THE TRANSFORM FUNCTION
    def test_transform(self):
        transformer = IntegerTransformer()
        transformer.fit(self.data)
        transformed_data = transformer.transform(self.data)

        pd.testing.assert_frame_equal(
            transformed_data.reset_index(drop=True),
            self.expected_transformed.reset_index(drop=True),
            check_dtype=False
        )

    def test_transform_without_fit(self):
        # TESTING THAT THE TRANSFORM RAISES AN ERROR IF FIT IS NOT CALLED FIRST
        transformer = IntegerTransformer()

        with self.assertRaises(AttributeError):
            transformer.transform(self.data)

if __name__ == "__main__":
    unittest.main()