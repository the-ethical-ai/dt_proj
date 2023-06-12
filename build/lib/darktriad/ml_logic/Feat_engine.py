'''
Initial feature engineering function
'''
# Packages/Libraries Used
import pandas as pd
import numpy as np

def feature_engineering(X: pd.DataFrame) -> pd.DataFrame:
    # Compute row averages per trait (new column per average)
    # Column name format: traitType_Avg

    # Separating the questions
    narcis_df = X[['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9']]
    mach_df = X[['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9']]
    psych_df = X[['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']]

    # Calculating the average score per trait per user
    X['Narcissism_Avg'] = narcis_df.mean(axis=1).round(3)
    X['Psychopathy_Avg'] = psych_df.mean(axis=1).round(3)
    X['Machiavellianism_Avg'] = mach_df.mean(axis=1).round(3)

    # -1 means below typical range
    # 0 means typical range
    # 1 means above typical range

    ### Making narcissism category
    tmp = []
    for i in X['Narcissism_Avg']:
        if i < 2.222:
            tmp.append(-1)
        elif i >= 2.222 and i < 3.778:
            tmp.append(0)
        else:
            tmp.append(1)
    X['Narcissism_Category'] = tmp

    ### Making psychopathy category
    tmp = []
    for i in X['Psychopathy_Avg']:
        if i < 2:
            tmp.append(-1)
        elif i >= 2 and i < 4:
            tmp.append(0)
        else:
            tmp.append(1)
    X['Psychopathy_Category'] = tmp

    ### Making machiavellian category
    tmp = []
    for i in X['Machiavellianism_Avg']:
        if i < 2.222:
            tmp.append(-1)
        elif i >= 2.222 and i < 4.889:
            tmp.append(0)
        else:
            tmp.append(1)
    X['Machiavellianism_Category'] = tmp

    return X
