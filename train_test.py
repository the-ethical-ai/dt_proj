'''
Handles creating the new dataframes and splitting the data into training and
testing set.
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def train_test(X: pd.DataFrame):

    '''
    1. Creates 3 new dataframe (one for each targeted trait)
    2. Split each dataset into train-validation-test sets (70/30 train/test; 70/30 train/validation)

    Feature Dataframes Naming Format: X_psych, X_mach, X_narc
    Targets Naming Format: Y_psych, Y_mach, Y_narc
    Train Set Naming Format: X_train_psych, X_train_narc, X_train_mach

    '''

    ### (1)Create the dataframe with average psychopathy as target
    psych_questions = [f'P{int(i)}' for i in np.linspace(1, 9, 9)]

    X_psych = pd.DataFrame()

    # filling in the X_psych
    for i in X.columns:
        if i not in psych_questions:
            X_psych[f'{i}'] = X[i]

    # Creating the target
    Y_psych = X['Psychopathy_Category']


    ### (2) Create the dataframe with average narcissism as target
    narc_questions = [f'N{int(i)}' for i in np.linspace(1,9,9)]

    X_narc = pd.DataFrame()

    # filling in X_narc
    for i in X.columns:
        if i not in narc_questions:
            X_narc[f'{i}'] = X[i]

    # Creating the target
    Y_narc = X['Narcissism_Category']


    ### (3) Create the dataframe with average Machiavellianism as target
    mach_questions = [f'M{int(i)}' for i in np.linspace(1,9,9)]

    X_mach = pd.DataFrame()

    # filling in X_mach
    for i in X.columns:
        if i not in mach_questions:
            X_mach[f'{i}'] = X[i]

    # Creating the target
    Y_mach = X['Machiavellianism_Category']


    ### Splitting (1)




    ### Splitting (2)




    ### Splitting (3)




    ### RETURN DICTIONARY OF LISTS
        ### 3 X_trains, X_tests, X_validation
        ### 3 y_train, validations, and tests
