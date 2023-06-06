'''
Initial feature engineering function
'''
# Packages/Libraries Used
import pandas as pd


def feature_engineering(X: pd.DataFrame) -> pd.DataFrame

    ### Compute row averages per trait (new column per average)
    ### Column name format: traitType_Avg

    # Separating the questions
    narcis_df = X[['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9']]
    mach_df = X[['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9']]
    psych_df = X[['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']]

    # Calculating the average score per trait per user
    narcissism_Avg = narcis_df.mean(axis = 1).round(3),
    psychopathy_Avg = psych_df.mean(axis = 1).round(3),
    machievellianism_Avg = mach_df.mean(axis = 1).round(3)

    # Making the new columns for the average score per trait
    X['Narcissism_Avg'] = narcissism_Avg
    X['Psychopathy_Avg'] = psychopathy_Avg
    X['Machiavellianism_Avg'] = machievellianism_Avg


    ### Buckets (keep as integers) (new column per trait)
    ### Round to closest integer (<.5, down; >=.5, up)

    narc_cats = []  # short for narcissism_categories
    psych_cats = [] # same idea
    mach_cats = []  # same idea

    # Rounding each score and adding the rounded value to the respective lists
    for i in range(len(narcissism_Avg)):
        narc_cats.append(narcissism_Avg[i].round())
        psych_cats.append(psychopathy_Avg[i].round())
        mach_cats.append(machievellianism_Avg[i].round())

    # Adding the rounded averages (categories) as new columns
    X['Narcissism_Category'] = narc_cats
    X['Psychopathy_Category'] = psych_cats
    X['Machiavellianism_Category'] = mach_cats

    ### Returning the dataframe
    return X
