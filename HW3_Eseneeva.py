class CountVectorizer:

    import warnings

    def __init__(self, vocabulary=None):
        self.vocabulary = vocabulary

    @staticmethod
    def process_text(word_string: str, delimiter=' ') -> list:
        if not isinstance(word_string, str):
            raise ValueError('Type mismatch: object do not have .lower() method')
        return word_string.lower().split(delimiter)

    @staticmethod
    def extend_list(lists_of_words: list) -> list:
        corpus = []
        for word_list in lists_of_words:
            corpus.extend(word_list)

        return sorted(list(set(corpus)))

    def create_corpus_matrix(self, document: list) -> list:
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
        if isinstance(document[0], list):
            document = document[0]
        self.vocabulary = self.extend_list(map(self.process_text, document))
        x = self.create_corpus_matrix(document)
        return x

    def get_feature_names(self):
        if self.vocabulary is None:
            raise Warning('No fitted vocabulary provided')
        return self.vocabulary


vec = CountVectorizer()
test = ['Hello there how are ya doing', 'hellothere']
print(vec.fit_transform(test))
print(vec.get_feature_names())