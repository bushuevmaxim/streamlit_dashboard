import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X["transmission"] = X["transmission"].map(
            {"automatic": 0, "mechanical": 1})
        X['has_warranty'] = (~X['has_warranty']).astype(np.byte)
        X["state"] = X["state"].map({"owned": 1, "new": 2, "emergency": 0})
        for i in range(10):
            X[f'feature_{i}'] = (~X[f'feature_{i}']).astype(np.byte)
        return X
