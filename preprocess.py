'''
This file contains a function that clean the data and handles initial feature
engineering.
'''
#### Importing required packages
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

### Function definition

def preprocess(X: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates
    data_wo_dup = X.drop_duplicates()

    # Remove rows with missing values
    data_wo_na = data_wo_dup.dropna()

    # Remove the "source" column
    df_afterremove = data_wo_na.drop("source", axis=1)

    # Create a new column "US_resident" based on the "country" column
    df_afterremove['US_resident'] = np.where(df_afterremove["country"] == "US", 1, 0)

    # Remove the "country" column
    df_final = df_afterremove.drop("country", axis=1)
    column_names = list(df_final.columns[:-1])
    # Scale the remaining features using StandardScaler
    scaler = StandardScaler()
    df_final_scaled = scaler.fit_transform(df_final.iloc[:, :-1])

    # Convert the scaled array back to a DataFrame
    df_final_final = pd.DataFrame(df_final_scaled,columns=column_names)
    # final_dataframe = df_final_final.merge(df_final[["US_resident"]])
    final_dataframe = df_final_final.merge(df_final[["US_resident"]], left_index=True, right_index=True)

    return final_dataframe
