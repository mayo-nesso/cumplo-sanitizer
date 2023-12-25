import unittest
from unittest.mock import patch

from cumplo_sanitizer.src.cumplo_core import extract_active_and_late_ids


class TestExtractActiveAndLateIds(unittest.TestCase):
    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_20932_late_and_ok(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_[20932]_late_and_ok.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["20932"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, [])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_15572(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_15572_ok_but_then_not_paid.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["15572"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, ["15572"])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_20970(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_20970_ok_but_then_not_paid.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["20970"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, ["20970"])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_15731(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_15731_late_and_ok.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["15731"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, [])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_20970_uncollectible(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_20970_uncollectible.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = True

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["20970"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, ["20970"])
        self.assertCountEqual(uncollectible_ids, ["20970"])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_21033(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_21033_ok_and_late.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["21033"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, [])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_id_20970_collectible(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_id_20970_late_but_collectible.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["20970"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, ["20970"])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_completed_and_active(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_4completed_2active.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["21022", "20932", "20970", "15731", "21033", "15572"])
        self.assertCountEqual(active_ids, ["21033", "20932"])
        self.assertCountEqual(late_ids, [])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_6_collectibles(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_6_not_paid_but_collectible.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["20932", "15731", "21033", "20970", "15572", "21022"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, ["15731", "20932", "21022", "21033", "20970", "15572"])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_6_active(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_6active.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["15572", "21022", "20970", "21033", "20932", "15731"])
        self.assertCountEqual(active_ids, ["15572", "21022", "20970", "21033", "20932", "15731"])
        self.assertCountEqual(late_ids, [])
        self.assertCountEqual(uncollectible_ids, [])

    @patch("cumplo_sanitizer.src.cumplo_core.some_utils.is_date_past_grace_period")
    def test_extract_0_active(self, mock_is_date_past_grace_period):
        path = "./cumplo_sanitizer/tests/flujo_files/"
        path_to_file = path + "Resumen de flujos_6completed.xlsx"

        # Mock the is_date_past_grace_period function (uncollectible in case of late payment...)
        mock_is_date_past_grace_period.return_value = False

        # Call your function
        all_ids, active_ids, late_ids, uncollectible_ids = extract_active_and_late_ids(
            path_to_file, 60
        )

        # Add assertions here to verify the results
        self.assertCountEqual(all_ids, ["20932", "21033", "15731", "20970", "15572", "21022"])
        self.assertCountEqual(active_ids, [])
        self.assertCountEqual(late_ids, [])
        self.assertCountEqual(uncollectible_ids, [])
