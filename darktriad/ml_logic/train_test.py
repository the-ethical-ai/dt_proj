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
    2. Split each dataset into train-validation-test sets (70/30 train/test; 80/20 train/validation)

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

    # dropping non-relevant columns
    X_psych.drop(columns=['Psychopathy_Avg', 'Narcissism_Avg',
                          'Machiavellianism_Avg', 'Narcissism_Category',
                          'Psychopathy_Category', 'Machiavellianism_Category'],
                 inplace = True)

    # Creating the target
    y_psych = X['Psychopathy_Category']


    ### (2) Create the dataframe with average narcissism as target
    narc_questions = [f'N{int(i)}' for i in np.linspace(1,9,9)]

    X_narc = pd.DataFrame()

    # filling in X_narc
    for i in X.columns:
        if i not in narc_questions:
            X_narc[f'{i}'] = X[i]

    # dropping non-relevant columns
    X_narc.drop(columns=['Narcissism_Avg', 'Psychopathy_Avg',
                         'Narcissism_Category', 'Machiavellianism_Avg',
                          'Psychopathy_Category', 'Machiavellianism_Category'],
                 inplace = True)

    # Creating the target
    y_narc = X['Narcissism_Category']


    ### (3) Create the dataframe with average Machiavellianism as target
    mach_questions = [f'M{int(i)}' for i in np.linspace(1,9,9)]

    X_mach = pd.DataFrame()

    # filling in X_mach
    for i in X.columns:
        if i not in mach_questions:
            X_mach[f'{i}'] = X[i]

    # dropping non-relevant columns
    X_mach.drop(columns=['Machiavellianism_Avg', 'Psychopathy_Avg',
                         'Narcissism_Category', 'Narcissism_Avg',
                          'Psychopathy_Category', 'Machiavellianism_Category'],
                 inplace = True)

    # Creating the target
    y_mach = X['Machiavellianism_Category']


    ### Splitting (1)

    # train-test split
    X_train_psych, X_test_psych, y_train_psych, y_test_psych = train_test_split(
        X_psych, y_psych, test_size = 0.3, random_state = 84)

    # train-validation split
    X_train_psych, X_val_psych, y_train_psych, y_val_psych = train_test_split(
        X_train_psych, y_train_psych, test_size = 0.2, random_state = 84
    )

    ### Splitting (2)
    X_train_narc, X_test_narc, y_train_narc, y_test_narc = train_test_split(
        X_narc, y_narc, test_size=0.3, random_state=84
    )

    X_train_narc, X_val_narc, y_train_narc, y_val_narc = train_test_split(
        X_train_narc, y_train_narc, test_size=0.2, random_state=84
    )

    ### Splitting (3)
    X_train_mach, X_test_mach, y_train_mach, y_test_mach = train_test_split(
        X_mach, y_mach, test_size=0.3, random_state=84
    )

    X_train_mach, X_val_mach, y_train_mach, y_val_mach = train_test_split(
        X_train_mach, y_train_mach, test_size=0.2, random_state=84
    )

    ### RETURN DICTIONARY OF LISTS
        ### 3 X_trains, X_tests, X_validation
        ### 3 y_train, validations, and tests
    return {'X_trains': [X_train_psych, X_train_narc, X_train_mach],
            'X_tests': [X_test_psych, X_test_narc, X_test_mach],
            'X_validations': [X_val_psych, X_val_narc, X_val_mach],
            'y_trains': [y_train_psych, y_train_narc, y_train_mach],
            'y_tests': [y_test_psych, y_test_narc, y_test_mach],
            'y_vals': [y_val_psych, y_val_narc, y_val_mach]}
