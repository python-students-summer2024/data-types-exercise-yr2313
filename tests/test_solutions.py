from solutions import *

class Tests:

    def test_calculate_profit(self, capsys, monkeypatch):
        # test with sales of 3000, expecting 690 of profit
        monkeypatch.setattr("builtins.input", lambda x: 3000)
        calculate_profit()
        captured = capsys.readouterr() # capture print output
        assert captured.out.lower().strip() == "profit: $690.00"

        # test with sales of 10000, expecting 2300 of profit
        monkeypatch.setattr("builtins.input", lambda x: 10000)
        calculate_profit()
        captured = capsys.readouterr() # capture print output
        assert captured.out.lower().strip() == "profit: $2,300.00"

    def test_calculate_quotient_and_remainder(self, capsys, monkeypatch):
        input_values = ["5", "2"] # the mock values we will use for input
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        calculate_quotient_and_remainder()
        captured = capsys.readouterr() # capture print output
        expected = "2 goes into 5 a total of 2 times with a remainder of 1".lower().strip()
        assert captured.out.lower().strip() == expected

    def test_calculate_miles_per_gallon(self, capsys, monkeypatch):
        input_values = ["50", "2"] # the mock values we will use for input
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        calculate_miles_per_gallon()
        captured = capsys.readouterr() # capture print output
        expected = "Miles per gallon: 25.0".lower().strip()
        assert captured.out.lower().strip() == expected

    def test_align_text(self, capsys, monkeypatch):
        input_values = ["1", "200", "50"] # the mock values we will use for input
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        align_text()
        captured = capsys.readouterr() # capture print output
        expected = '''
Here are your prices!

Price #1: $    1.00
Price #2: $  200.00
Price #3: $   50.00
        ''' .lower().strip()
        ' '.join(expected.split()) # remove multiple whitespaces
        assert captured.out.lower().strip() == expected
