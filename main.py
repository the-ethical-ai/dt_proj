### MAIN FUNCTION

### Packages/Libraries
import sys
sys.path.insert(0, '..')

import functools

import pandas as pd
import numpy as np

from joblib import dump, load

from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
from darktriad.ml_logic.baseline import baseline
from darktriad.ml_logic.model import model
from darktriad.ml_logic.train_test import train_test
from darktriad.ml_logic.performance_eval import eval_model, pred

ticker = False

def prep():
    df = pd.read_csv("/Users/zemblanity/portfolio_projects/Dark_Triad/dark_triad/Data/SD3/data.csv",delimiter = '\t')
    df = preprocess(df)
    df = feature_engineering(df)
    train_test_Dict = train_test(df)
    print('train test split done')
    return train_test_Dict

def make_models():
    models = model(prep())
    return models

ticker = True

def save_model(models):
    dump(models, 'final_model.joblib')

def prediction(user_answers: list = None) -> list:
    print("\n⭐️ Use case: predict")
    if ticker == False:
        save_model(make_models())
    try:
        assert user_answers is not None

        models = load('final_model.joblib')
        assert models is not None
        print('\n✅ Models have been loaded')

        prediction = pred(models, user_answers)
        print("\n✅ Prediction Completed:", prediction, "\n")
        return prediction

    except Exception as e:
        print(f"\n❌ Error in prediction: {str(e)}\n")
        return []


if __name__ == '__main__':
    prediction(list(np.ones(27)) + [1])
