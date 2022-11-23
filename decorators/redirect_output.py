"""Decorator which redirects the output of the function to a file."""
import sys
from typing import Callable, Any


def redirect_output(filepath: str) -> Callable:
    """
    Decorator which redirects the output of the function to a file
    """
    original_write = sys.stdout.write

    def outer_wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs) -> Any:
            with open(filepath, 'a', encoding='utf8') as file_obj:
                sys.stdout.write = file_obj.write  # type: ignore
                result = func(*args, **kwargs)
                sys.stdout.write = original_write  # type: ignore

            return result

        return inner_wrapper

    return outer_wrapper


@redirect_output('./function_output.txt')
def calculate() -> None:
    """
    Function which illustrates the operation of the decorator redirect_output
    """
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()

    with open('function_output.txt', encoding='utf8') as fd:
        for line in fd.readlines():
            print(line)
