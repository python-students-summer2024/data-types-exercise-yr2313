from solutions import *


class Tests:
    def test_calculate_profit(self, capsys, monkeypatch):
        # test with sales of 3000, expecting 690 of profit
        inputs = ["3000", "10000"]  # the mock values we will use for input
        mock_values = inputs.copy()
        expecteds = ["profit: $690.00", "profit: $2,300.00"]
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        for i in range(len(mock_values)):
            mock_data = mock_values[i]
            expected = expecteds[i]
            calculate_profit()
            captured = capsys.readouterr()  # capture print output
            actual = captured.out.lower().strip()
            assert (
                expected == actual
            ), f'Expected the calculate_profit() function to print "{expected}" when the user input the value, "{mock_data}"; instead, it printed "{actual}".'

    def test_calculate_quotient_and_remainder(self, capsys, monkeypatch):
        inputs = ["5", "2"]  # the mock values we will use for input
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        calculate_quotient_and_remainder()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out.lower().strip()
        expected = (
            "2 goes into 5 a total of 2 times with a remainder of 1".lower().strip()
        )
        assert (
            expected == actual
        ), f'Expected the calculate_quotient_and_remainder() function to print "{expected}" when the user input the values, {mock_values}; instead, it printed "{actual}".'

    def test_calculate_miles_per_gallon(self, capsys, monkeypatch):
        inputs = ["50", "2"]  # the mock values we will use for input
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        calculate_miles_per_gallon()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out.lower().strip()
        actual = " ".join(actual.split())
        expected = "Miles per gallon: 25.0".lower().strip()
        expected = " ".join(expected.split())
        assert (
            expected in actual
        ), f'Expected the printed output of the calculate_miles_per_gallon() function to include "{expected}" when the user input the values, {mock_values}; instead, it printed "{actual}".'

    def test_align_text(self, capsys, monkeypatch):
        inputs = ["1", "200", "50"]  # the mock values we will use for input
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        align_text()
        captured = capsys.readouterr()  # capture print output
        expected = """
Here are your prices!

Price #1: $    1.00
Price #2: $  200.00
Price #3: $   50.00
        """.lower().strip()
        expected = " ".join(expected.split())  # remove multiple whitespaces
        actual = captured.out.lower().strip()
        actual = " ".join(actual.split())
        assert (
            expected == actual
        ), f'Expected the align_text() function to print "{expected}" when the user input the values, {mock_values}; instead, it printed "{actual}".'
