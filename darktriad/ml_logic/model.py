### Add the packages and libraries
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from lightgbm import LGBMClassifier
from sklearn.pipeline import make_pipeline

import lightgbm as lgb
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, max_error, explained_variance_score, mean_absolute_percentage_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def model(X: dict) -> dict:

    '''
    Returns a dictionary containing 3 models (one for each dark triad trait).
    Models have been fit on training sets.
    Uses random_state = 84.
    '''
    ### Separating out the training-validation-testing sets

    #X_train
    X_train_psych = X["X_trains"][0]
    X_train_narc = X["X_trains"][1]
    X_train_march = X["X_trains"][2]

    y_train_psych = X["y_trains"][0]
    y_train_narc = X["y_trains"][1]
    y_train_march = X["y_trains"][2]

    #X_validations
    X_vals_psych = X["X_validations"][0]
    X_vals_narc = X["X_validations"][1]
    X_vals_march = X["X_validations"][2]

    y_vals_psych = X["y_vals"][0]
    y_vals_narc = X["y_vals"][1]
    y_vals_march = X["y_vals"][2]

    #X_test
    X_test_psych = X["X_tests"][0]
    X_test_narc = X["X_tests"][1]
    X_test_march = X["X_tests"][2]

    y_test_psych = X["y_tests"][0]
    y_test_narc = X["y_tests"][1]
    y_test_march = X["y_tests"][2]


    ### Psychopathy model
    # Step 1: Define parameter grid for hyperparameter tuning
    param_grid = {
        'learning_rate': [0.1, 0.01,0.01],
        'n_estimators': [50, 100, 150],
        'max_depth': [4, 6, 10],
        'colsample_bytree': [0.7,0.9],
        'subsample': [0.6 ,0.7, 0.9],
        'min_child_samples': [1, 5, 8]
    }

    # Step 2: Initialize LGBMRegressor estimattor
    estimator = lgb.LGBMClassifier(random_state=84)

    # Step 3: Initalise Grid Search with 3-fold cross validation and fit model
    model_psych = GridSearchCV(estimator=estimator,
                         param_grid=param_grid,
                         cv=5,
                         n_jobs=-1,
                         scoring='accuracy')
    model_psych.fit(X_train_psych, y_train_psych)

    #model_psych.score(X_vals_psych,y_vals_psych)


    ### Narcissism model

    # Step 1: Define parameter grid for hyperparameter tuning
    param_grid = {
        'learning_rate': [0.1, 0.01, 0.001],
        'n_estimators': [50, 100, 150, 200],
        'max_depth': [4, 6, 20],
        'colsample_bytree': [0.6,0.7,0.9],
        'subsample': [0.5, 0.7, 0.9],
        'min_child_samples': [1, 5]
    }

    # Step 2: Initialize LGBMRegressor estimattor
    estimator = lgb.LGBMClassifier(random_state=84)

    # Step 3: Initalise Grid Search with 3-fold cross validation and fit model
    model_narc = GridSearchCV(estimator=estimator,
                         param_grid=param_grid,
                         cv=5,
                         n_jobs=-1,
                         scoring='accuracy')
    model_narc.fit(X_train_narc, y_train_narc)

    #model_narc.score(X_train_narc, y_train_narc)


    ### Machiavellianism model
    param_grid = {
        'learning_rate': [1 , 0.1, 0.01],
        'n_estimators': [40, 50, 100],
        'max_depth': [2, 4, 6, 10],
        'colsample_bytree': [0.6, 0.7,0.9],
        'subsample': [0.6, 0.7, 0.9],
        'min_child_samples': [1, 5,6,7]}


    # Step 2: Initialize LGBMRegressor estimattor
    estimator = lgb.LGBMClassifier(random_state=84)

    # Step 3: Initalise Grid Search with 3-fold cross validation and fit model
    model_march = GridSearchCV(estimator=estimator,
                         param_grid=param_grid,
                         cv=5,
                         n_jobs=-1,
                         scoring='accuracy')
    model_march.fit(X_train_march, y_train_march)

    #model_march.score(X_train_march, y_train_march)

    ### RETURN 3 models
    return {'Psychopathy_Model': model_psych,
            'Narcissism_Model': model_narc,
            'Machiavellianism_Model': model_march,
            'test_sets': [X_test_psych, X_test_narc, X_test_march,
                          y_test_psych, y_test_narc, y_test_march]}
