""" CountVectorizer implementaion """
from typing import List, Optional


class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.
    """
    def __init__(self):
        self.feature_names = None

    def get_feature_names(self) -> Optional[List[str]]:
        """
        Get list of tokens after the model has trained
        :return feature_names: Optional[List[str]]
            None if the model hasn't been trained yet.
            Otherwise, returns all unique words.
        """
        return self.feature_names

    def fit_transform(self, text: List[str]) -> List[List[int]]:
        """
        Learn the vocabulary dictionary and return document-term matrix
        :param text: List[str]
            Sentences, in which all words are only separated by space.
        :return count_matrix: List[List[int]]
            Document-term matrix.
        """
        unique_words = set()
        ordered_words = []
        doc_term_matrix = []

        # Building words set
        for sent in text:
            for word in sent.lower().split():
                if word not in unique_words:
                    ordered_words.append(word)
                    unique_words.add(word)

        self.feature_names = ordered_words

        # Building document term matrix
        for sent in text:
            counter = dict.fromkeys(ordered_words, 0)
            for word in sent.lower().split():
                counter[word] += 1

            doc_term_matrix.append(list(counter.values()))

        return doc_term_matrix


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    assert vectorizer.get_feature_names() == [
        'crock',
        'pot',
        'pasta',
        'never',
        'boil',
        'again',
        'pomodoro',
        'fresh',
        'ingredients',
        'parmesan',
        'to',
        'taste'
    ]
    assert count_matrix == [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
