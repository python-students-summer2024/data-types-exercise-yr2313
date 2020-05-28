import unittest
import solution
import io
import builtins
from contextlib import redirect_stdout
from unittest.mock import MagicMock

class Testing(unittest.TestCase):

    def test_return_name(self):
        self.assertEqual(solution.return_name(), 'Bob')

    def test_print_name(self):
        # capture printed output
        with io.StringIO() as buf, redirect_stdout(buf):
            solution.print_name()
            actual = buf.getvalue().strip() # remove line break from stdout
            self.assertEqual(actual, 'Bob')

    def test_input_name(self):
        old_input = builtins.input # so we can teardown later
        builtins.input = MagicMock(return_value='Bob') # setup
        self.assertEqual(solution.input_name(), 'Bob')
        builtins.input = old_input # teardown

