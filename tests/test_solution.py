import solution

class Tests:

    def test_return_name(self):
        assert solution.return_name() == 'Bob'

    def test_print_name(self, capsys):
        # capture printed output
        solution.print_name()
        captured = capsys.readouterr() # capture print output
        assert captured.out.strip() == 'Bob'
