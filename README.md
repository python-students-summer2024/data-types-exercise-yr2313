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

The file named `solution.py` contains several functions that must be completed in order for the program to work. Each function contains a description of what it should do.

The only modifications you must make in order to complete this assignment are to these functions in this one file.

### Run the program

To run the program, run the file named `main.py`. The code in this file makes use those functions you have modified in `solution.py` to produce and output the Mad Lib text.

### Verify the output is correct

Running the program should ask for the user to input several words (adjectives, nouns, verbs, etc), and then generate and output the text of Lewis Carrol's Jabberwocky with those words inserted in Mad Lib style.

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. If the functions have been completed correctly, all tests should pass. You should not edit any files in the `test` directory.
