
The model is organized in three main parts: the Pipeline, the Pre-Processing Pipeline, and the Transformations.

# The Pipeline:
It's the central part of the model. The class MyPipeline integrates the preprocessor, the model, the search strategy, and the evaluation metric. All these elements can be adjusted separately. 
How it works:
    1. Initiatie the MyPipeline class - here you must include as parameters: 'model', 'preprocessing', and 'score_metric', respectively.
    2. Fit the pipeline to the train and test sets. - .fit()
    3. Obtain de predictions - .predict()
    4. Perform the search - .tune() - to specify: 'X', 'y', 'strategy' - it will take RandomSearchCV and GridSearchCV as search strategies. 
    5. Obtain a list of the best parameters, according to the evaluation metric specified - get_params()
    6. Once the search is completed, the model is saved with the best-performing hyperparameters, for future fittings.

# The Pre-Processing Pipeline
It iterates through the specified transformations so they can be applied through one command. It takes a list of the transformations as an input. Here, is where the order of tranformations can be controlled. Specifications about order requirements are found within the transformation subclasses' header comments.

# The Transformation Class
It is an abstract base class containing, as child classes, all the transformations to be applied. The base class specifies that all subclasses must contain a .transform() method and, optionally, a .fit() method.

## SCALABILITY

The pipeline can very easily be scaled. New transformations and feature engineering can be added to the pre-processing pipeline by adding new scripts into the folder. This ensures easy access to all the transformation features as well as limited interaction with the already existing features. Moreover, the Transformation class ensures that all features contained within it will be compatible with the model application end of the pipeline.

The only potential conflict might arise from the order of application of certain transformations. In such cases, the potential requirements must be specified within the function declaration.