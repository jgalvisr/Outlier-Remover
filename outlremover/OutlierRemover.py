from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

# Se crea un transformador personalizado que convierte valores anómalos en nulos
class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = pd.DataFrame(X).copy()
        for i in range(X.shape[1]):
            x = X.iloc[:, i].copy()
            for j in range(X.shape[0]):
                if (i == 2 and x[j] == 0) or (i != 2 and x[j] <= 1):
                    X.iloc[j, i] = np.nan
        return X