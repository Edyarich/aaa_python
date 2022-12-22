"""Command Line Interface for Pizza Delivery Service"""
import random
from typing import (
    Optional,
    Callable,
)
import click
from pizza import (
    BasePizza,
    Margherita,
    PepperoniPizza,
    Hawaiian
)

MENU = (
    Margherita(),
    PepperoniPizza(),
    Hawaiian()
)
MAX_DELIVERY_TIME = 4
MAX_PICKUP_TIME = 2
DEFAULT_BAKING_TIME = 10


@click.group()
def cli():
    """
    A plug
    :return: None
    """


def log(format_str: Optional[str] = None) -> Callable:
    """
    Decorator which prints the function name and its return value
    :param format_str: str
    :return: Calable
    """
    def outer_wrapper(func: Callable) -> Callable:
        nonlocal format_str
        if format_str is None:
            format_str = func.__name__ + ' - {} seconds!'

        def inner_wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            nonlocal format_str
            return format_str.format(result)  # type: ignore

        return inner_wrapper

    return outer_wrapper


@log('🍴 Приготовили за {} с!')
def bake(pizza: BasePizza) -> int:
    """
    :param pizza: BasePizza
    :return baking_time (in seconds): int
    """
    return DEFAULT_BAKING_TIME + len(pizza.content)


@log('🚗 Доставили за {} с!')
def deliver() -> int:
    """
    :return deliver_time (in seconds): int
    """
    return random.randint(0, MAX_DELIVERY_TIME)


@log('🏠 Забрали за {} с!')
def pickup() -> int:
    """
    :return pickup_time (in seconds): int
    """
    return random.randint(0, MAX_PICKUP_TIME)


def get_pizza_by_name(pizza_name: str) -> BasePizza:
    """
    Factory method which returns BasePizza instance
    :param pizza_name: str
    :return: BasePizza
    """
    for dish in MENU:
        if isinstance(dish, BasePizza) and dish.name == pizza_name:
            return dish

    return BasePizza(pizza_name, 'L', [])


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool):
    """
    API function which prints information about an order
    :param pizza_name: str
    :param delivery: bool
    :return: None
    """
    pizza = get_pizza_by_name(pizza_name)
    print(bake(pizza))

    if delivery:
        print(deliver())
    else:
        print(pickup())


@cli.command()
def menu():
    """
    API function which prints the menu
    :return: None
    """
    for dish in MENU:
        print('-', dish)


if __name__ == '__main__':
    cli()
