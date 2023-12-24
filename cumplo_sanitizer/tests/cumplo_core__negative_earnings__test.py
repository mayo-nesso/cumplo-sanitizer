import unittest

import pandas as pd

from cumplo_sanitizer.src.cumplo_core import (
    find_negative_earning_ids,
)


class TestFindNegativeEarningIds(unittest.TestCase):
    def test_negative_earnings(self):
        """Test with data containing negative earnings"""
        data = {
            "RemateID": [1, 1, 2, 2],
            "Abono": [200, 300, 200, 500],
            "Cargo": [400, 600, 100, 250],
        }
        df = pd.DataFrame(data)
        result = find_negative_earning_ids(df)
        self.assertIn(1, result)  # RemateID 1 has negative earnings
        self.assertNotIn(2, result)  # RemateID 2 does not

    def test_no_negative_earnings(self):
        """Test with data having no negative earnings"""
        data = {
            "RemateID": [1, 1, 2, 2],
            "Abono": [300, 300, 200, 250],
            "Cargo": [200, 100, 100, 50],
        }
        df = pd.DataFrame(data)
        result = find_negative_earning_ids(df)
        self.assertEqual(len(result), 0)  # No RemateID with negative earnings

    def test_empty_dataframe(self):
        """Test with an empty DataFrame"""
        df = pd.DataFrame(columns=["RemateID", "Abono", "Cargo"])
        result = find_negative_earning_ids(df)
        self.assertEqual(result, [])  # Should return an empty list
