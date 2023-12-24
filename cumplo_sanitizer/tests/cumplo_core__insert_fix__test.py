import csv
import os
import unittest
from unittest.mock import patch

import pandas as pd

from cumplo_sanitizer.src.cumplo_core import (
    _create_return_row,
    _get_fix_data,
    insert_fix,
)


class TestGetFixData(unittest.TestCase):
    def setUp(self):
        """Create a sample CSV file for testing"""
        self.test_csv_file = "test_fix_data.csv"
        with open(self.test_csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Header1", "Header2", "Header3"])  # example headers
            writer.writerow(["data1", "data2", "data3"])
            writer.writerow(["data4", "data5", "data6"])

    def tearDown(self):
        """Clean up by deleting the test file after tests"""
        os.remove(self.test_csv_file)

    def test_get_fix_data(self):
        """Test reading data from a valid CSV file"""
        result = _get_fix_data(self.test_csv_file)
        self.assertEqual(len(result), 2)  # Two data rows
        self.assertEqual(result[0], ["data1", "data2", "data3"])  # First data row

    def test_get_fix_data_empty_file(self):
        """Test reading data from an empty CSV file"""
        with open(self.test_csv_file, "w", newline="") as file:  # Create an empty file
            pass
        result = _get_fix_data(self.test_csv_file)
        self.assertEqual(result, [])  # Empty list for empty file

    def test_get_fix_data_invalid_file(self):
        """Test reading data from a non-existent CSV file"""
        with self.assertRaises(FileNotFoundError):
            _get_fix_data("non_existent_file.csv")


class TestCreateReturnRow(unittest.TestCase):
    def test_create_return_row(self):
        """Test the _create_return_row function with standard input"""
        r_id = "234234"
        actor = "Invs Invs"
        date = "2023-01-01"
        abono = "1111"
        cargo = "0"

        expected_result = {
            "Fecha": pd.Timestamp("2023-01-01"),
            "Cargo": 0,
            "Abono": 1111,
            "Descripción": "fix_ Pago de inversión, solicitud Credito Invs Invs 234234",
            "Tipo": "Fix",
            "Solicitud": "Credito Invs Invs 234234",
            "RemateID": "234234",
            "Actor": "Invs Invs",
        }

        result = _create_return_row(r_id, actor, date, abono, cargo)
        self.assertEqual(result, expected_result)

    def test_create_return_row_with_invalid_date(self):
        """Test the _create_return_row function with an invalid date format"""
        r_id = "123"
        actor = "John Doe"
        date = "invalid-date"
        abono = "500"
        cargo = "300"

        with self.assertRaises(ValueError):
            _create_return_row(r_id, actor, date, abono, cargo)

    def test_create_return_row_with_nonnumeric_values(self):
        """Test the _create_return_row function with non-numeric abono and cargo"""
        r_id = "123"
        actor = "John Doe"
        date = "2023-01-01"
        abono = "abc"
        cargo = "xyz"

        with self.assertRaises(ValueError):
            _create_return_row(r_id, actor, date, abono, cargo)


class TestInsertFix(unittest.TestCase):
    def setUp(self):
        """Set up a sample DataFrame for testing"""
        self.original_df = pd.DataFrame(
            {
                "Fecha": [pd.Timestamp("2023-01-01"), pd.Timestamp("2023-01-02")],
                "Cargo": [100, 200],
                "Abono": [50, 150],
                "Descripción": ["desc1", "desc2"],
                "Tipo": ["Type1", "Type2"],
                "Solicitud": ["Solic1", "Solic2"],
                "RemateID": ["R1", "R2"],
                "Actor": ["Actor1", "Actor2"],
            }
        )

    @patch("cumplo_sanitizer.src.cumplo_core._get_fix_data")
    @patch("cumplo_sanitizer.src.cumplo_core._create_return_row")
    def test_insert_fix(self, mock_create_return_row, mock_get_fix_data):
        """Test the insert_fix function with valid data"""
        # Mock the return values of the dependent functions
        mock_get_fix_data.return_value = [["123", "John Doe", "2023-01-03", "500", "300"]]
        mock_create_return_row.return_value = {
            "Fecha": pd.Timestamp("2023-01-03"),
            "Cargo": 300,
            "Abono": 500,
            "Descripción": "fix_ Pago de inversión, solicitud Credito John Doe 123",
            "Tipo": "Fix",
            "Solicitud": "Credito John Doe 123",
            "RemateID": "123",
            "Actor": "John Doe",
        }

        expected_df = pd.DataFrame(
            {
                "Fecha": [
                    pd.Timestamp("2023-01-01"),
                    pd.Timestamp("2023-01-02"),
                    pd.Timestamp("2023-01-03"),
                ],
                "Cargo": [100, 200, 300],
                "Abono": [50, 150, 500],
                "Descripción": [
                    "desc1",
                    "desc2",
                    "fix_ Pago de inversión, solicitud Credito John Doe 123",
                ],
                "Tipo": ["Type1", "Type2", "Fix"],
                "Solicitud": ["Solic1", "Solic2", "Credito John Doe 123"],
                "RemateID": ["R1", "R2", "123"],
                "Actor": ["Actor1", "Actor2", "John Doe"],
            }
        )

        result_df = insert_fix(self.original_df, "fixdata.csv")
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_insert_fix_no_csv_path(self):
        """Test the insert_fix function with no CSV path specified"""
        result_df = insert_fix(self.original_df, None)
        pd.testing.assert_frame_equal(result_df, self.original_df)
