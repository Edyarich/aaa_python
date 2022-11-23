""" To begin with, let's replace the write method of the sys.stdout object
with a function that, before each call to the original data recording function
in stdout, prints the current timestamp to the text."""
import sys
import time


original_write = sys.stdout.write


def my_write(string_text: str) -> None:
    """
    my_write output: timestamp: text
    Example: Tue Nov 22 16:38:38 2022: 1, 2, 3
    """
    if len(string_text.rstrip()) == 0:
        return

    original_write(time.asctime() + ': ' + string_text + '\n')


if __name__ == '__main__':
    sys.stdout.write = my_write  # type: ignore
    print('1, 2, 3')
    sys.stdout.write = original_write  # type: ignore
