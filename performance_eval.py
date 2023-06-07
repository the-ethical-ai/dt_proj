'''
Makes predictions and evaulates the models.

All of these steps must be performed on all 3 models.
'''
### Import the packages and models
from model import model
from sklearn.metrics import accuracy_score

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


def pred(sets: dict, user_answers: list):

    ### Call the model
    models = model(sets)
    psych_model = models['Psychopathy_Model']
    narc_model = models['Narcissism_Model']
    mach_model = models['Machiavellianism_Model']

    y_pred_psych = psych_model.predict(user_answers[:18])

    ### RETURN 3 predicted classes based on user's answers.
    return y_pred_psych
