import unittest
import pandas as pd
from your_module.imputer import Imputer

class TestImputer(unittest.TestCase):
    def setUp(self):
        """
        Set up sample data and expected results for testing.
        """
        self.train_data = pd.DataFrame({
            'Album Name': ['A', 'A', 'B', 'B', 'C', 'C'],
            'Column1': [1, None, 3, None, 5, None],
            'Column2': [None, 2, None, 4, None, 6]
        })

        self.test_data = pd.DataFrame({
            'Album Name': ['A', 'B', 'C'],
            'Column1': [None, None, None],
            'Column2': [None, None, None]
        })

        self.expected_train_output = pd.DataFrame({
            'Column1': [1.0, 1.0, 3.0, 3.0, 5.0, 5.0],
            'Column2': [2.0, 2.0, 4.0, 4.0, 6.0, 6.0]
        })

        self.expected_test_output = pd.DataFrame({
            'Column1': [1.0, 3.0, 5.0],
            'Column2': [2.0, 4.0, 6.0]
        })

        self.imputer = Imputer(group_by_column='Album Name')

    def test_fit_and_transform_train(self):
        """
        Test fit and transform on the training set.
        """
        self.imputer.fit(self.train_data)
        transformed_data = self.imputer.transform(self.train_data)
        pd.testing.assert_frame_equal(transformed_data, self.expected_train_output)

    def test_transform_test(self):
        """
        Test transform on the test set using means from the training set.
        """
        self.imputer.fit(self.train_data)
        transformed_data = self.imputer.transform(self.test_data)
        pd.testing.assert_frame_equal(transformed_data, self.expected_test_output)

    def test_fit_without_group_column(self):
        """
        Test behavior when the grouping column is missing during fit.
        """
        data_without_group = self.train_data.drop(columns=['Album Name'])

        with self.assertRaises(KeyError):
            self.imputer.fit(data_without_group)

    def test_transform_without_fit(self):
        """
        Test behavior when transform is called without calling fit first.
        """
        with self.assertRaises(RuntimeError):
            self.imputer.transform(self.train_data)

    def test_no_numerical_columns(self):
        """
        Test behavior when no numerical columns are present in the data.
        """
        data_no_numerical = pd.DataFrame({
            'Album Name': ['A', 'B', 'C'],
            'Category': ['X', 'Y', 'Z']
        })

        self.imputer.fit(data_no_numerical)
        transformed_data = self.imputer.transform(data_no_numerical)

        expected_output = pd.DataFrame({
            'Category': ['X', 'Y', 'Z']
        })

        pd.testing.assert_frame_equal(transformed_data, expected_output)

if __name__ == '__main__':
    unittest.main()