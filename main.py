'''
Calls all functions
'''
# Imports
import sys
sys.path.insert(0, '..')

import numpy as np
import pandas as pd
from preprocess import preprocess
from Feat_engine import feature_engineering
from train_test import train_test
from model import model
from baseline import baseline

def main():
    df = pd.read_csv("/home/saikotdasjoy/code/Saikot1997/dt_proj/raw_data/data.csv",delimiter = '\t')
    df = preprocess(df)
    df = feature_engineering(df)
    train_test_Dict = train_test(df)
    baseline_val_accuracy_psych, baseline_val_accuracy_narc, baseline_val_accuracy_mach = baseline(train_test_Dict)

    model_return = model(train_test_Dict)

if __name__ == '__main__':
    main()
