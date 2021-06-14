from unittest import TestCase
from src.exercises import ex2

import pandas as pd


class TestEX2(TestCase):
    def test_filter_polls_data(self):
        covid_approvals_path = "../../data/covid_approval_polls.csv"
        approvals_df = pd.read_csv(covid_approvals_path)
        concerns_path = "../../data/covid_concern_polls.csv"
        concerns_df = pd.read_csv(concerns_path)
        pollster_path = "../../data/pollster_ratings.xlsx"
        pollster_df = pd.read_excel(pollster_path, engine="openpyxl")

        message = "Check function return a tuple with 2 Dataframes"
        actual = ex2.filter_polls_data(approvals_df, concerns_df, pollster_df)
        expected = tuple()
        self.assertEqual(type(actual), type(expected), message)
        # self.fail()
