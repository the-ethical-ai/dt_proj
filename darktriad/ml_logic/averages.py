"""
This file contains the get_plot_data function, which returns a dataframe with the
average scores per trait type from data set 1 (SD3).
"""

### Packages/libraries
import pandas as pd
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering

def get_plot_data():
    ### retrieve dataset
    df = pd.read_csv("https://raw.githubusercontent.com/Habeus-Crimpus/Dark_Triad/main/data.csv",delimiter = '\t')

    ### Preprocessing
    df = preprocess(df)

    ### Feature Engineering
    df = feature_engineering(df)

    ### Selecting the relevant columns
    return df[['Narcissism_Avg', 'Psychopathy_Avg', 'Machiavellianism_Avg']]
