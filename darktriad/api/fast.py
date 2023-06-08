
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
from darktriad.ml_logic.train_test import train_test
from darktriad.ml_logic.model import model
from darktriad.ml_logic.performance_eval import pred
from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

df = pd.read_csv(URL)
df = preprocess(df)
df = feature_engineering(df)
splits = train_test(df)
models = model(splits)


@app.get("/predict")
def predict(
    sets: models,
    user_answers: list
):
    y_predictions = pred(sets, user_answers)
