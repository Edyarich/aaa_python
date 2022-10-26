""" Tf-idf """
from typing import List, Optional
import math


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
        words_set = set()
        words_list = []
        doc_term_matrix = []

        # Building words set
        for sent in text:
            for word in sent.lower().split():
                if word not in words_set:
                    words_list.append(word)
                    words_set.add(word)

        self.feature_names = words_list

        # Building document term matrix
        for sent in text:
            counter = dict.fromkeys(words_list, 0)
            for word in sent.lower().split():
                counter[word] += 1

            doc_term_matrix.append(list(counter.values()))

        return doc_term_matrix


class TfidfTransformer:
    """
    Convert matrix with count of words in each sentence to tf-idf matrix
    """
    @staticmethod
    def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Get tf-matrix from count-matrix
        :param count_matrix: List[List[int]]
            Matrix with count of words in each sentence.
        :return freq_mat: List[List[float]]
            Tf-matrix.
        """
        if len(count_matrix) == 0:
            return []

        freq_mat = []

        for count_row in count_matrix:
            freq_mat.append(
                list(map(lambda count: count / sum(count_row), count_row)))

        return freq_mat

    @staticmethod
    def idf_transform(count_matrix: List[List[int]]) -> List[float]:
        """
        Get idf-matrix from count-matrix
        :param count_matrix: List[List[int]]
            Matrix with count of words in each sentence.
        :return idf_mat: List[float]
            Idf-matrix.
        """
        if len(count_matrix) == 0:
            return []

        idf_mat = []
        k_documents = len(count_matrix)
        k_tokens = len(count_matrix[0])

        for i in range(k_tokens):
            k_docs_with_ith_token = sum(
                count_matrix[j][i] > 0 for j in range(k_documents))
            idf = math.log((1 + k_documents) / (1 + k_docs_with_ith_token)) + 1
            idf_mat.append(round(idf, 1))

        return idf_mat

    def fit_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Get tf-idf-matrix from count-matrix
        :param count_matrix: List[List[int]]
            Matrix with count of words in each sentence.
        :return tf_idf_mat: List[List[float]]
            Tf-idf matrix.
        """
        tf_matrix = TfidfTransformer.tf_transform(count_matrix)
        idf_matrix = TfidfTransformer.idf_transform(count_matrix)

        tf_idf_mat = []

        for tf_row in tf_matrix:
            tf_idf_row = [tf_row[i] * idf_matrix[i] for i in range(len(tf_row))]
            tf_idf_mat.append(list(map(lambda x: round(x, 3), tf_idf_row)))

        return tf_idf_mat


class TfidfVectorizer(CountVectorizer):
    """
    Convert a collection of text documents to a matrix of tf-idf features.
    """
    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, text: List[str]) -> List[List[float]]:
        """
        Get tf-idf-embeddings from the corpus
        :param text: List[str]
            Sentences, in which all words are only separated by space.
        :return tf_idf_mat: List[List[float]]
            Tf-idf matrix.
        """
        count_matrix = super().fit_transform(text)
        tf_idf_mat = self.transformer.fit_transform(count_matrix)

        return tf_idf_mat


if __name__ == '__main__':
    small_corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(small_corpus)
    feat_names = [
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
    tfidf = [
        [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    ]

    assert vectorizer.get_feature_names() == feat_names
    assert tfidf == tfidf_matrix
