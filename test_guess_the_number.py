import unittest
from unittest.mock import patch
import builtins
import guess_the_number

class TestGuessTheNumber(unittest.TestCase):

    @patch('guess_the_number.random.randint', return_value=50)
    @patch('builtins.input', side_effect=['30', '70', '50'])
    @patch('builtins.print')
    def test_guessing_game(self, mock_print, mock_input, mock_randint):
        guess_the_number.guess_the_number()
        # Check that the print statements for too low, too high, and correct guess are called
        mock_print.assert_any_call("Too low! Try again.")
        mock_print.assert_any_call("Too high! Try again.")
        mock_print.assert_any_call("Congratulations! You guessed the number correctly.")

    @patch('guess_the_number.random.randint', return_value=42)
    @patch('builtins.input', side_effect=['abc', '42'])
    @patch('builtins.print')
    def test_invalid_input(self, mock_print, mock_input, mock_randint):
        guess_the_number.guess_the_number()
        # Check that invalid input message is printed
        mock_print.assert_any_call("Please enter a valid integer.")
        mock_print.assert_any_call("Congratulations! You guessed the number correctly.")

if __name__ == '__main__':
    unittest.main()
