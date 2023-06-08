
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
from darktriad.ml_logic.train_test import train_test
from fastapi import FastAPI
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

#app.state.model = load_model()

@app.get("/predict")
def predict(user_answers: #default):

    model = app.state.model
    assert model is not None

    y_pred = model.predict(user_answers)
    return dict(fare_amount=float(y_pred))





@app.get("/")
async def root():
    return {"message": "Hello World"}
