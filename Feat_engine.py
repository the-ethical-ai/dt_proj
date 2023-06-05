'''
Initial feature engineering function
'''
import pandas as pd


def feature_engineering(X: pd.DataFrame) -> pd.DataFrame

    ### Compute row averages per trait (new column per average)
    ### Column name format: traitType_Avg



    ### Buckets (keep as integers) (new column per trait)
    ### Round to closest integer (<.5, down; >=.5, up)
