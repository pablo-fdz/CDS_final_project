_Authors_: Ferran Boada, Blanca Jiménez and Pablo Fernández.

---

This repository contains the foundations for a scalable machine learning library (in the folder `ml_library`) that integrates all of the typical steps of the pipeline (EDA, preprocessing, hyperparameter tuning and prediction). It is designed considering the principles of object-oriented programming (e.g., inheritance and polymorphism) and to ensure compatibility with `scikit-learn`'s machine learning classes. This work was the final project for the subject _Computing for Data Science_ of BSE's Master's Program _Data Science for Decision-Making_, in 2024-2025.

---

The library is organized in three main parts: the (main) Pipeline class (`my_pipeline`), the Pre-Processing Pipeline (`preprocessing_pipeline`), and the Transformations.

# 1. The Pipeline
It's the central part of the model. The class `MyPipeline` integrates the preprocessor class, the model, hyperparameter tuning, the search strategy, and the evaluation metric. All of these elements can be adjusted separately through different methods.

How it works:

1. Initiatie the MyPipeline class - here you must include as parameters: `model` (a `scikit-learn` model with `.fit` and `.predict` methods), `preprocessing` (an instance of the `PreprocessingPipeline` class, which defaults to an empty pipeline if none is specified), and `score_metric` (a `scikit-learn` function for computing a metric), respectively.

2. Fit the pipeline to the train and test sets. - `.fit()`
   
3. Perform the search of the optimal hyperparameters - `.tune()`  - to specify: `X`, `y`, `strategy` - it will take `scikit-learn`'s `RandomSearchCV` and `GridSearchCV` as search strategies. It then saves the optimal hyperparameters of the model and updates the `model` attribute within the `MyPipeline` instance with the optimal hyperparameters.

4. Obtain the predictions - `.predict()` 

5. Obtain a list of the best parameters, according to the evaluation metric specified - `get_params()` 

# 2. The Pre-Processing Pipeline
It iterates through the specified transformations so they can be applied through one command. It takes a list of the transformations as an input. Here, is where the order of tranformations can be controlled. Specifications about order requirements are found within the transformation subclasses' header comments.

# 3. The `Transformation` Class
It is an abstract base class containing, as child classes, all the transformations to be applied. The base class specifies that all subclasses must contain a `.transform()`  method and, optionally, a `.fit()`  method (which ensures compatibility with `scikit-learn`'s hyperparameter search strategies).

# 4. Scalability

The pipeline can very easily be scaled. New transformations and feature engineering can be added to the pre-processing pipeline by adding new scripts into the folder. This ensures easy access to all the transformation features as well as limited interaction with the already existing features. Moreover, the `Transformation` class ensures that all features contained within it will be compatible with the model application end of the pipeline.

The only potential conflict might arise from the order of application of certain transformations. In such cases, the potential requirements must be specified within the function declaration, so it should be controlled by the user.

# 5. Sample implementation

To see an example of the implementation of the library, check out the Jupyter Notebook `pipeline_notebook.ipynb`.
