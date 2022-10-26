""" Практика №2 """


class BasePokemon:
    """
    Pokemon class
    """
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __repr__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    """
    Mixin for changing pokemon type to emoji
    """
    pokemon_to_empji = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __repr__(self):
        name_and_type = super().__repr__()
        name, pokemon_type = name_and_type.split('/')

        if pokemon_type in self.pokemon_to_empji:
            return name + '/' + self.pokemon_to_empji[pokemon_type]

        return name_and_type


class Pokemon(EmojiMixin, BasePokemon):
    """
    Pokemon class with emoji
    """


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
