import ml_library as ml
import pandas as pd
from sklearn.linear_model import LogisticRegression
import csv
import json
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
import joblib


#directory model
MODEL_DIR= "data/model.pkl"

# Read the CSV file and convert to JSON
csv_file_path = 'data/spotify-2024.csv'
json_file_path = 'data/sample_input.json'

data = []

with open(csv_file_path, 'r', encoding='latin-1') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # Automatically maps rows to dictionary using headers
    for row in csv_reader:
        data.append(row)

# Write the JSON to a file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV converted to JSON and saved to {json_file_path}")

data= pd.read_json('data/sample_input.json')
data = pd.DataFrame(data)

print("json loaded")

target = 'Explicit Track'
features = data.drop(columns=[target])
target_data = data[target]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target_data, test_size=0.2, random_state=42)

print(X_train)

# Create preprocessing pipeline
nan_remover = ml.NanRemover()
integer_transformer = ml.IntegerTransformer()
standardizer = ml.Standardizer()
features = ml.FeatureEngineering()
pipeline = ml.PreprocessingPipeline([nan_remover, integer_transformer, standardizer])

# Create model (can be any model that supports fit and predict)
logreg = LogisticRegression(max_iter = 5000,
                            penalty = 'l2',
                            fit_intercept = True)

# Create pipeline
pipeline = ml.MyPipeline(model = logreg, preprocessing = pipeline)

# Fit model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, MODEL_DIR)

print("Model saved as model.pkl")
