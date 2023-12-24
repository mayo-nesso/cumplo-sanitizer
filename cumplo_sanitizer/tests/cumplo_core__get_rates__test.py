import unittest
from unittest.mock import patch

import pandas as pd
from pyxirr import InvalidPaymentsError

from cumplo_sanitizer.src.cumplo_core import _get_rates


class TestGetRates(unittest.TestCase):
    def test_get_rates_normal_case(self):
        """Test _get_rates with a normal case"""
        data = {
            "Fecha": [pd.Timestamp("2023-01-01"), pd.Timestamp("2023-01-10")],
            "Abono": [1000, 500],
            "Cargo": [900, 450],
        }
        df = pd.DataFrame(data)
        diff_days, mrate_iir, rate_iir_yr, rate_xir = _get_rates(df)
        self.assertEqual(diff_days, 9)
        self.assertAlmostEqual(mrate_iir, (1500 / 1350) - 1)
        # Add further assertions for rate_iir_yr and rate_xir based on expected values

    def test_get_rates_normal_case2(self):
        """Test _get_rates with a normal case"""
        data = {
            "Fecha": [
                pd.Timestamp("2022-03-04"),
                pd.Timestamp("2022-04-14"),
                pd.Timestamp("2022-04-14"),
            ],
            "Abono": [0, 181.0, 507403.0],
            "Cargo": [500000, 0, 0],
        }
        df = pd.DataFrame(data)
        diff_days, mrate_iir, rate_iir_yr, rate_xir = _get_rates(df)
        self.assertEqual(diff_days, 41)
        self.assertAlmostEqual(mrate_iir, 1.5168 / 100)
        self.assertAlmostEqual(rate_iir_yr, 13.6512 / 100)
        self.assertAlmostEqual(rate_xir, 14.34138 / 100)

    def test_get_rates_empty_df(self):
        """Test _get_rates with an empty DataFrame"""
        df = pd.DataFrame(columns=["Fecha", "Abono", "Cargo"])
        result = _get_rates(df)
        self.assertEqual(result, (None, None, None, None))

    @patch("pyxirr.xirr")
    def test_get_rates_xirr_error(self, mock_xirr):
        """Test _get_rates when xirr calculation fails"""
        mock_xirr.side_effect = InvalidPaymentsError
        data = {
            "Fecha": [pd.Timestamp("2023-01-01"), pd.Timestamp("2023-01-10")],
            "Abono": [1000, 500],
            "Cargo": [900, 450],
        }
        df = pd.DataFrame(data)
        diff_days, mrate_iir, rate_iir_yr, rate_xir = _get_rates(df)
        self.assertIsNone(rate_xir)
        # Assert other values as well
