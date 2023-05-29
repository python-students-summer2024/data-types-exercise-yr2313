# Data Types Practice

A little assignment about the various kinds of data built into Python by default

## Clone this repository

First, clone this repository to your local computer, using Visual Studio Code's cloning feature.

Helpful video:

- [cloning a code repository from GitHub to your local machine](https://www.youtube.com/watch?v=axcny0o1NYo).

## Set up Visual Studio Code

Once cloned, set Visual Studio Code to be suitable for Python development using the "command palette":

- set the interpreter to a Python 3.x interpreter, such as that by [`Anaconda`](https://www.anaconda.com/).
- set the linter to by `pylint`.
- set the test framework to be `pytest`.

Helpful video:

- [Setting up Visual Studio Code for Python development](https://www.youtube.com/watch?v=xsXMzyK1M4I)

## Modify the code

The file named `solutions.py` contains several functions that must be completed in order for the program to work. Each function contains a description of what it should do.

The only modifications you must make in order to complete this assignment are to these functions in this one file.

### Run the program

To run the program, run the file named `main.py`. The code in this file makes use those functions you have modified in `solutions.py` to produce and output the text.

A best practice is to focus on one problem at a time. Comment out any lines in the `main.py` program that run parts of the code you are not interested in trying out at the moment.

### Verify the output is correct

Make sure that your program behaves as expected when you run it. Review the requirements and compare your work to them. Any requests for user input or printed output should match exactly the samples given in the instructions. Pay attention to details, such as the number of spaces, the number of newlines, the use of punctuation, etc.

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. If the functions have been completed correctly, all tests should pass. You should not edit any files in the `test` directory.

If the tests do not appear, or seem to never stop loading, or you experience other problems with them, open up a Terminal window and run the command, `pytest --collect-only`, to see whether there are any errors in the code that prevent the tests from being discovered. If there are no errors reported from that command, try running the tests directly from the Terminal with the command, `pytest`.
