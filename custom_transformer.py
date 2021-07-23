from sklearn.base import BaseEstimator, TransformerMixin
from gensim.models import Word2Vec
import numpy as np

#custome transfromer incorporating word2vec model by gensim
class CustomWord2Vec(BaseEstimator, TransformerMixin):

    def __init__(self, model=None):
        self.w2v_model = model

    def get_params(self, deep=False):
        return {'model': self.w2v_model}

    def sent2vec(self, sentence):
        sent_vector = np.zeros(50)
        for word in sentence:
            if word in self.w2v_model.wv:
                sent_vector += self.w2v_model.wv[word]
        return sent_vector / len(sentence)

    def fit(self, X, y=None):
        transformed_text = [text.split() for text in X]
        self.w2v_model = Word2Vec(transformed_text, size=50, min_count=5, workers=6)
        return self

    def transform(self, documents):
        output = []
        for document in documents:
            output.append(self.sent2vec(document.split()))
        return np.array(output)