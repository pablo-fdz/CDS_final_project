import ml_library as ml
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV, cross_validate
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
standardizer = ml.Standardizer()
pipeline = ml.PreprocessingPipeline([standardizer])

# Create model
logreg = LogisticRegression(max_iter = 200,
                            penalty = 'l2',
                            fit_intercept = True)

# Create pipeline
pipeline = ml.MyPipeline(model = logreg, preprocessing = pipeline, score_metric = accuracy_score)

# Prediction BEFORE tuning
print('Prediction before hyperparameter tuning:')
pipeline.fit(X_train, y_train)
print(pipeline.predict(X_test))
print(pipeline.model.get_params())

# Hyperparameter tuning
search_strategy = RandomizedSearchCV(
    pipeline,
    param_distributions = {
        'model__C': uniform(loc=0.01, scale=10),
    },
    n_iter = 10,
    random_state=0
)
pipeline.tune(X = X_train, y = y_train, strategy = search_strategy)

# Prediction AFTER tuning
print('Prediction after hyperparameter tuning:')
pipeline.fit(X_train, y_train)
print(pipeline.predict(X_test))
print(pipeline.model.get_params())