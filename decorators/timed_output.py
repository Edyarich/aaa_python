"""Perform the same logic as in the change_write.py"""
import sys
import time
from typing import Callable


def timed_output(function: Callable):
    """Mark the output of the function with timestamps"""
    original_write = sys.stdout.write

    def my_write(string_text: str):
        if len(string_text.rstrip()) == 0:
            return

        original_write(time.asctime() + ': ' + string_text + '\n')

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        function(*args, **kwargs)
        sys.stdout.write = original_write

    return wrapper


@timed_output
def print_greeting(name: str) -> None:
    """Function which illustrates the decorator timed_output"""
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
