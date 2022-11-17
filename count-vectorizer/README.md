## Условие
Реализуйте класс `CountVectorizer`, имеющий
- метод `fit_transform`
- метод `get_feature_names`

Ограничения:
- пользоваться внешними пакетами запрещено
- решение должно быть в *.py файлах
- не должно быть замечаний PEP8
- решение загружено на github до 13.10.2022 18:00 MSK
- если умеешь, то напиши проверки/тесты

## Примеры
```python
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',    
    'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    print(count_matrix)
    Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
```