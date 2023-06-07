'''
Baseline model
'''
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def baseline(train_test_Dict):

    # Select the desired columns for training data
    X_train_psych = train_test_Dict["X_trains"][0].iloc[:,:-2]
    X_train_narc = train_test_Dict["X_trains"][1].iloc[:,:-2]
    X_train_mach = train_test_Dict["X_trains"][2].iloc[:,:-2]

    #  Select the desired columns for test data
    X_test_psych = train_test_Dict["X_tests"][0].iloc[:,:-2]
    X_test_narc = train_test_Dict["X_tests"][1].iloc[:,:-2]
    X_test_mach = train_test_Dict["X_tests"][2].iloc[:,:-2]

    #  Select the desired columns for validation data
    X_val_psych = train_test_Dict["X_validations"][0].iloc[:,:-2]
    X_val_narc = train_test_Dict["X_validations"][1].iloc[:,:-2]
    X_val_mach = train_test_Dict["X_validations"][2].iloc[:,:-2]

    # Select the desired columns for Target data
    y_train_psych, y_train_narc, y_train_mach = train_test_Dict['y_trains']
    y_test_psych, y_test_narc, y_test_mach = train_test_Dict['y_tests']
    y_val_psych, y_val_narc, y_val_mach = train_test_Dict['y_vals']

    nb_psych = GaussianNB()
    nb_narc = GaussianNB()
    nb_mach = GaussianNB()

    nb_psych.fit(X_train_psych, y_train_psych)
    nb_narc.fit(X_train_narc, y_train_narc)
    nb_mach.fit(X_train_mach, y_train_mach)

    y_pred_val_psych = nb_psych.predict(X_val_psych)
    y_pred_val_narc = nb_narc.predict(X_val_narc)
    y_pred_val_mach = nb_mach.predict(X_val_mach)


    baseline_val_accuracy_psych = accuracy_score(y_val_psych, y_pred_val_psych)
    baseline_val_accuracy_narc = accuracy_score(y_val_narc, y_pred_val_narc)
    baseline_val_accuracy_mach = accuracy_score(y_val_mach, y_pred_val_mach)


    return baseline_val_accuracy_psych, baseline_val_accuracy_narc, baseline_val_accuracy_mach
