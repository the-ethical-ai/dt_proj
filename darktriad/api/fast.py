
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
from darktriad.ml_logic.train_test import train_test
from darktriad.ml_logic.model import model
from darktriad.ml_logic.performance_eval import pred
from darktriad.interface.main import prediction
from fastapi import FastAPI
from joblib import dump, load
import numpy as np
import pandas as pd
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],  # Allows all origins
#    allow_credentials=True,
#    allow_methods=["*"],  # Allows all methods
#    allow_headers=["*"],  # Allows all headers
#)

models = load('final_model.joblib')

@app.get('/a')
def dummy(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
    q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,
    q24,q25,q26,q27,q28):

    answer_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
    q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,
    q24,q25,q26,q27,q28]

    vals = [int(i) for i in answer_list]
    return str(type(vals))

@app.get("/predict")
def predict(
    user_answers #= [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,1]
    #q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
    #q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,
    #q24,q25,q26,q27,q28
):

    #answer_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
    #q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,
    #q24,q25,q26,q27,q28]

    #vals = [int(i) for i in answer_list]
    vals = [int(i) for i in user_answers.strip('[]').split(',')]
    sample = prediction(vals)
    #sample = prediction([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,1])
    return {'Psych_Pred': sample[0],
            'Narc_Pred': sample[1],
            'Mach_Pred': sample[2]}


@app.get("/")
async def root():
    return {"message": "BASE"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=4000)
