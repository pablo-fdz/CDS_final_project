import ml_library as ml
import pandas as pd
from typing import Callable
from collections.abc import Callable
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from scipy.stats import uniform
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Data
train_data = pd.DataFrame(data = {
    'A': [1, 5, 6, 8, 10, 10, 15, 16, 7, 8],
    'B': [0, 3, 50, 2000, 2, 76, 62, 23, 1, 56],
    'target': [1, 0, 0, 0, 1, 0, 1, 1, 0, 1]
})

X_train = train_data[['A', 'B']]
y_train = train_data['target']

test_data = pd.DataFrame(data = {
    'A': [8, 6, 5, 3, 8, 23, 5, 6, 7, 8],
    'B': [8, 5, 59, 2333, 1, 123, 45, 23, 7, 19]
})

X_test = test_data[['A', 'B']]

# Create preprocessing pipeline
nan_remover = ml.NanRemover()
standardizer = ml.Standardizer()
integer_transformer = ml.IntegerTransformer()
imputer = ml.Imputer()
pipeline = ml.PreprocessingPipeline([nan_remover, integer_transformer, imputer, standardizer])

# Create model
logreg = LogisticRegression(max_iter = 200,
                            penalty = 'l2',
                            fit_intercept = True)

# Create pipeline
pipeline = ml.MyPipeline(model = logreg, preprocessing = pipeline, score_metric = accuracy_score)

cv_scores = cross_validate(estimator = pipeline, X = X_train, y = y_train)

print(cv_scores)