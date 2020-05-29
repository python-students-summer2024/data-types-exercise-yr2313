import unittest
import solution
import io
import builtins
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

class Testing(unittest.TestCase):

    def test_return_name(self):
        self.assertEqual(solution.return_name(), 'Bob')

    def test_print_name(self):
        # capture printed output
        with io.StringIO() as buf, redirect_stdout(buf):
            solution.print_name()
            actual = buf.getvalue().strip() # remove line break from stdout
            self.assertEqual(actual, 'Bob')

            
if __name__ == '__main__':
    unittest.main()