"""Pizza ingredients"""


class Ingredient:
    """
    Base class which provides interface for pizza ingredient
    """
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return self.name


class TomatoSauce(Ingredient):
    """
    Tomato sauce ingredient
    """
    def __init__(self):
        super().__init__('tomato sauce')


class Mozzarella(Ingredient):
    """
    Mozzarella ingredient
    """
    def __init__(self):
        super().__init__('mozzarella')


class Tomato(Ingredient):
    """
    Tomato ingredient
    """
    def __init__(self):
        super().__init__('tomatoes')


class Pepperoni(Ingredient):
    """
    Pepperoni ingredient
    """
    def __init__(self):
        super().__init__('pepperoni')


class Chicken(Ingredient):
    """
    Chicken ingredient
    """
    def __init__(self):
        super().__init__('chicken')


class Pineapple(Ingredient):
    """
    Pineapple ingredient
    """
    def __init__(self):
        super().__init__('pineapples')
