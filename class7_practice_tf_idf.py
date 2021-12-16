import warnings  # https://stackoverflow.com/questions/25650710/should-import-be-inside-or-outside-a-python-class
import math


class CountVectorizer:
    """
    This class produces a document-term matrix for a given document.
    Parameters:
    document : list of strings
        If document contains more than 1 list,  only 1st one will be processed.
    Attributes:
    vocabulary : list
        List of words in alphabetic order used to construct a document-term matrix.
    """

    def __init__(self, vocabulary=None):
        self.vocabulary = vocabulary

    @staticmethod
    def process_text(word_string: str, delimiter=' ') -> list:

        """
        Process the string - convert to lowercase and split to words by delimiter.
        """

        if not isinstance(word_string, str):
            raise ValueError('Type mismatch: object do not have .lower() method')
        return word_string.lower().split(delimiter)

    @staticmethod
    def extend_list(lists_of_words: list) -> list:

        """
        Convert a list of lists into a 1-D list.
        """

        corpus = []
        for word_list in lists_of_words:
            corpus.extend(word_list)

        return sorted(list(set(corpus)))

    def create_corpus_matrix(self, document: list) -> list:

        """
        Creates a document-term matrix based on previously fitted vocabulary.
        """

        corpus_matrix = []
        vocab = self.vocabulary

        for doc in document:
            doc_dict = dict.fromkeys(vocab, 0)
            for word in doc.split(' '):
                word = word.lower()
                if word in doc_dict.keys():
                    doc_dict[word] += 1
            corpus_matrix.append(list(doc_dict.values()))

        return corpus_matrix

    def fit_transform(self, document: list) -> list:

        """
        Fit a vocabulary for a given document (list of strings) and return the document-term matrix of a document.
        """

        if isinstance(document[0], list):
            document = document[0]
        self.vocabulary = self.extend_list(map(self.process_text, document))

        return self.create_corpus_matrix(document)

    def get_feature_names(self):

        """
        Returns fitted vocabulary.
        """

        if self.vocabulary is None:
            raise Warning('No fitted vocabulary provided')

        return self.vocabulary


class TfIdfTransformer:

    def tf_transform(self, matrix):
        """
        Returns vector of TFs
        """
        return [[round(float(j) / sum(i), 3) for j in i] for i in matrix]

    def idf_transform(self, matrix: list) -> list:
        """
        Returns of IDFs
        """
        A = [0] * len(matrix[0])
        matrix = [[1 if i > 0 else 0 for i in doc_matrix] for doc_matrix in matrix]

        for i in matrix:
            A = [(x + y) for x, y in zip(i, A)]

        p = len(matrix) + 1
        idfs = []
        for i in A:
            idfs.append(round(math.log(p / (i + 1)) + 1, 1))

        return idfs

    def tf_idf_transformer(self, matrix: list) -> list:
        """
        Returns TF-IDF transformation
        """
        tfs = self.tf_transform(matrix)
        idfs = self.idf_transform(matrix)
        return [[round(idf * tf, 3) for idf, tf in zip(idfs, tfs_n)] for tfs_n in tfs]


class TfIdfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__(self)
        self._tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, document: list) -> list:
        corpus_matrix = super().fit_transform(document)
        return self._tfidf_transformer.tf_idf_transformer(corpus_matrix)


if __name__ == '__main__':
    vec = TfIdfVectorizer()
    vec2 = TfIdfTransformer()
    doc = ['Hello there how are ya doing', 'hellothere']
    count_matrix = vec.fit_transform(doc)
    print(vec.create_corpus_matrix(doc))
    print(vec.get_feature_names())
    print(vec2.tf_transform(count_matrix))
    print(vec2.idf_transform(count_matrix))
    print(vec2.tf_idf_transformer(count_matrix))