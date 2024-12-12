import ml_library as ml
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data
train_data = pd.DataFrame(data = {
    'A': [1, 5, 6, 8, 10],
    'B': [0, 3, 50, 2000, 2],
    'target': [1, 0, 0, 0 ,1]
})

X_train = train_data[['A', 'B']]
y_train = train_data['target']

test_data = pd.DataFrame(data = {
    'A': [8, 6, 5, 3, 8],
    'B': [8, 5, 59, 2333, 1]
})

X_test = test_data[['A', 'B']]

# Create preprocessing pipeline
nan_remover = ml.NanRemover()
standardizer = ml.Standardizer()
pipeline = ml.PreprocessingPipeline([nan_remover, standardizer])

# Create model
logreg = LogisticRegression(penalty = 'l2')

# Create pipeline
pipeline = ml.MyPipeline(model = logreg, preprocessing = pipeline)

# Fit model
pipeline.fit(X_train, y_train)
prediction = pipeline.predict(X_test)

print(prediction)