# CDS_final_project

Library structure:
1. *Data loading*: loading the data from multiple types of sources. For now, it could just load the data from a single type of source. Also, it could convert the data into a data frame.
2. *EDA*: numerical and graphical exploratory data analysis. Organize folders by type of analysis (graphical/numerical), type of variables, etc. 
3. *Preprocessing*: chonkiest module of the library. It should be composed of multiple types of preprocessors (including data cleaning, feature creation, encoding of categorical variables, etc.), where each class could be child classes of an abstract `Transformation` class, with the method .transform(data) which returns data. Each preprocessor should take, as input, some data, and return the transformed data. Also, it would be interesting to create a transformation pipeline that takes in (i.e., is a composition) of the `Transformation` class, and the initialization of which includes each of the preprocessing steps you want to include in the training/cross-validation. This should be compatible then with step 4, for hyperparameter-tuning + cross-validation.
4. *Hyperparameter-tuning, cross-validation and model evaluation*. Perform grid search / randomized search or any other algorithm that searches for the best hyperparameters through cross validation. As input, it should receive the transformation pipeline from step 3, so that the transformation is applied separately (but in the same way) to training and validation. It should also consider for the possibility of evaluation with different models, and maybe return an object which contains the optimal hyperparameters found through cross-validation.
5. *Prediction*: predicts new data with the optimal hyperparameters and the chosen model found in step 4. 

Dataset: https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024/code
