'''
Calls all functions
'''
# Imports
import sys
sys.path.insert(0, '..')

import numpy as np
import pandas as pd


from pathlib import Path
from colorama import Fore, Style
from dateutil.parser import parse
from ml_logic.preprocess import preprocess
from ml_logic.Feat_engine import feature_engineering
from ml_logic.train_test import train_test
from ml_logic.model import model
from ml_logic.baseline import baseline
from ml_logic.performance_eval import eval_model,pred

def load():
    df = pd.read_csv("/home/saikotdasjoy/code/Saikot1997/dt_proj/raw_data/data.csv",delimiter = '\t')
    df = preprocess(df)
    df = feature_engineering(df)
    train_test_Dict = train_test(df)
    baseline_val_accuracy_psych, baseline_val_accuracy_narc, baseline_val_accuracy_mach = baseline(train_test_Dict)

    return train_test_Dict

def prediction(user_answers: list = None) -> list:
    print("\n⭐️ Use case: predict")
    try:
        assert user_answers is not None

        train_test_Dict = load()
        model_return = model(train_test_Dict)
        assert model_return is not None

        prediction = pred(train_test_Dict, user_answers)
        print("\n✅ Prediction done:", prediction, "\n")
        return prediction

    except Exception as e:
        print(f"\n❌ Error in prediction: {str(e)}\n")
        return []


if __name__ == '__main__':
    prediction()
