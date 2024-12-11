import ml_library as ml
import pandas as pd

data = pd.DataFrame(data = {
    'A': [1, 5, 6, 8, 10],
    'B': [0, 3, 50, 2000, 2]
})

# Create the desired transformations
nan_remover = ml.NanRemover()
standardizer = ml.Standardizer()

# Create preprocessing pipeline
preprocessing_pipeline = ml.PreprocessingPipeline([nan_remover, standardizer])

# Apply (fit and transform) transformations
preprocessing_pipeline.fit(data)
new_data = preprocessing_pipeline.transform(data)

print(new_data)