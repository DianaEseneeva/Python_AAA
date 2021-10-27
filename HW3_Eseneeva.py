import warnings  # https://stackoverflow.com/questions/25650710/should-import-be-inside-or-outside-a-python-class


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
        x = self.create_corpus_matrix(document)
        return x  # можно сразу

    def get_feature_names(self):

        """
        This function returns fitted vocabulary.
        """

        if self.vocabulary is None:
            raise Warning('No fitted vocabulary provided')
        return self.vocabulary


if __name__ == '__main__':
    vec = CountVectorizer()
    test = ['Hello there how are ya doing', 'hellothere']
    print(vec.fit_transform(test))
    print(vec.get_feature_names())
