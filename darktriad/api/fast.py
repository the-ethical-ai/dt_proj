import glob
import joblib
import pandas as pd
from colorama import Fore, Style
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from darktriad.ml_logic.performance_eval import pred
from fastapi import HTTPException


app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


def load_model():
    print(Fore.BLUE + "\nLoad latest model from local registry..." + Style.RESET_ALL)

    # Get the latest model version name by the timestamp on disk
    local_model_directory = "/home/saikotdasjoy/code/Saikot1997/dt_proj/trained_models.joblib"
    latest_model = joblib.load(local_model_directory)
    print("✅ Model loaded from local disk")
    return latest_model

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict")
def predict(user_answers: List[int]):
    # Load the models
    models = load_model()

    # Make predictions using the loaded models
    y_predictions = pred(models, user_answers)

    # Return the predictions
    return y_predictions
