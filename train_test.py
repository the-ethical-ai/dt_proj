'''
Handles creating the new dataframes and splitting the data into training and
testing set.
'''

import pandas as pd

def train_test(X: pd.DataFrame):

    '''
    1. Creates 3 new dataframe (one for each targeted trait)
    2. Split each dataset into train-validation-test sets (70/30 train/test; 70/30 train/validation)

    Naming format: X_train_psych, X_train_narc, X_train_mach
    '''

    ### (1)Create the dataframe with average psychopathy as target




    ### (2) Create the dataframe with average narcissism as target



    ### (3) Create the dataframe with average Machiavellianism as target



    ### Splitting (1)




    ### Splitting (2)




    ### Splitting (3)




    ### RETURN DICTIONARY OF LISTS
        ### 3 X_trains, X_tests, X_validation
        ### 3 y_train, validations, and tests
