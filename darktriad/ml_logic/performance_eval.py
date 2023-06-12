'''
Makes predictions and evaulates the models.

All of these steps must be performed on all 3 models.
'''
### Import the packages and models
from darktriad.ml_logic.model import model
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np

def eval_model(sets: dict) -> dict:
    ### Getting each of the models
    psych_model = sets['Psychopathy_Model']
    narc_model = sets['Narcissism_Model']
    mach_model = sets['Machiavellianism_Model']

    ### Getting the test sets
    X_test_psych = sets['test_sets'][0]
    y_test_psych = sets['test_sets'][3]

    X_test_narc = sets['test_sets'][1]
    y_test_narc = sets['test_sets'][4]

    X_test_mach = sets['test_sets'][2]
    y_test_mach = sets['test_sets'][5]


    ### Psychopathy Model Evaluation
    y_pred_psych = psych_model.predict(X_test_psych)
    psych_model_score = accuracy_score(y_pred_psych, y_test_psych)

    ### Narcissism Model Evaluation
    y_pred_narc = narc_model.predict(X_test_narc)
    narc_model_score = accuracy_score(y_pred_narc, y_test_narc)

    ### Machiavellianism Model Evaulation
    y_pred_mach = mach_model.predict(X_test_mach)
    mach_model_score = accuracy_score(y_pred_mach, y_test_mach)

    return {'Psychopathy_Model_Accuracy': psych_model_score,
            'Narcissism_Model_Accuracy': narc_model_score,
            'Machiavellianism_Model_Accuracy': mach_model_score}


def pred(sets: dict, user_answers: list) -> list:

    ### Call the model
    psych_model = sets['Psychopathy_Model']
    narc_model = sets['Narcissism_Model']
    mach_model = sets['Machiavellianism_Model']

    ### Making pandas series out of the user answers
    psych_series = pd.Series(user_answers[:18] + [user_answers[-1]],
                             index = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7',
                                      'M8', 'M9', 'N1', 'N2', 'N3', 'N4', 'N5',
                                      'N6', 'N7', 'N8', 'N9', 'US_resident'])
    narc_series = pd.Series(user_answers[:9] + user_answers[18:27] + [user_answers[-1]],
                            index = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7',
                                     'M8', 'M9', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6',
                                     'P7', 'P8', 'P9', 'US_resident'])
    mach_series = pd.Series(user_answers[9:27] + [user_answers[-1]],
                            index = ['N1', 'N2', 'N3','N4', 'N5', 'N6', 'N7',
                                     'N8', 'N9', 'P1', 'P2', 'P3', 'P4', 'P5',
                                     'P6', 'P7', 'P8', 'P9', 'US_resident'])

    ### Making predictions
    y_pred_psych = psych_model.predict(psych_series.to_numpy().reshape(1,-1))
    y_pred_narc = narc_model.predict(narc_series.to_numpy().reshape(1,-1))
    y_pred_mach = mach_model.predict(mach_series.to_numpy().reshape(1,-1))

    ### RETURN 3 predicted classes based on user's answers.
    return {
        'y_pred_psych': y_pred_psych,
        'y_pred_narc': y_pred_narc,
        'y_pred_mach': y_pred_mach
        }
