# tf-idf
## Задание #1: count vectorizer
Реализуйте класс CountVectorizer, имеющий метод `fit_transform`
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

## Задание #2: term frequency
Реализуйте функцию `tf_transform`
```python
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]
tf_matrix = tf_transform(count_matrix)

print(tf_matrix)
Out: [
    [0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143]
]
```

## Задание #3: inverse document-frequency
Реализуйте функцию `idf_transform`
```python
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]
idf_matrix = idf_transform(count_matrix)

print(idf_matrix)
Out: [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]
```

## Задание #4: tf-idf transformer
Реализуйте класс `TfidfTransformer`, имеющий метод `fit_transform`
```python
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]
transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count_matrix)

print(tfidf_matrix)
Out: [
    [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
]
```

## Задание #5: tf-idf vectorizer
Реализуйте класс `TfidfVectorizer`, имеющий метод `fit_transform`
```python
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
'fresh', 'ingredients', 'parmesan', 'to', 'taste']

print(tfidf_matrix)
Out: [
    [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
]
```
