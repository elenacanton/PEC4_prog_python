import unittest
from src.exercises import ex1


class TestEX1(unittest.TestCase):

    def test_times_words(self):
        path_csv = '../data/covid_approval_polls.csv'
        search_word = 'Huffington Post'
        message = "Check Huffington Post should appear 112 times"

        actual = ex1.count_times_word(path_csv, search_word)
        expected = f"The pattern {search_word} appears 112 times"
        self.assertEqual(actual, expected, message)


if __name__ == "__main__":`
    unittest.main()
