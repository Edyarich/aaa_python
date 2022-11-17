## Задание #1: Pokemon/магический метод
Дан класс `Pokemon`
```python
class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        
    def to_str(self):
        return f'{self.name}/{self.poketype}'
```
Замените метод `to_str`
```python
bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
print(bulbasaur)
Out: 'Bulbasaur/grass'
```

## Задание #2: Pokemon/миксин
Напишите миксин `EmojiMixin`, который модифицирует метод `__str__`.  
Заменяет категорию покемона на эмоджи:
- grass => 🌿
- fire => 🔥
- water => 🌊
- electric => ⚡
```python
pikachu = Pokemon(name='Pikachu', category='electric')
print(pikachu)
Out: 'Pikachu/⚡'
```