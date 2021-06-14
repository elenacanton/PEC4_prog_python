from unittest import TestCase
from src.exercises.ex4 import get_min_grade
from src.exercises.ex4 import count_total_participation
from src.exercises import ex2
from pandas._testing import assert_frame_equal


class TestEX4(TestCase):
    def test_get_min_grade(self):
        actual = get_min_grade("A")
        expected = "A"
        self.assertEqual(expected, actual)

        actual = get_min_grade("A/B")
        expected = "B"
        self.assertEqual(expected, actual)

        actual = get_min_grade("C/B")
        expected = "C"
        self.assertEqual(expected, actual)

        actual = get_min_grade("A+")
        expected = "A"
        self.assertEqual(expected, actual)

        actual = get_min_grade("D-")
        expected = "D"
        self.assertEqual(expected, actual)

    def count_total_participation(self):
        covid_approvals_path = "../../data/covid_approval_polls.csv"
        approvals_df = pd.read_csv(covid_approvals_path)
        concerns_path = "../../data/covid_concern_polls.csv"
        concerns_df = pd.read_csv(concerns_path)
        pollster_path = "../../data/pollster_ratings.xlsx"
        pollster_df = pd.read_excel(pollster_path, engine="openpyxl")
        data_filtered = ex2.filter_polls_data(approvals_df, concerns_df, pollster_df)

        message = "Check function return an integer with total participants"
        actual = ex4.count_total_participation(data_filtered[concerns_df])
        expected = int
        self.assertEqual(type(actual), type(expected), message)
