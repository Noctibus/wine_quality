from fastapi import FastAPI
from model import prediction
app = FastAPI()


@app.get("/api/predict{data}")
async def predict(data:str):
    # predit le resultat en fonction des donnees passes en parametre de la route
    if data is None:
        return {"error": "no data"}
    else:
        fixed_acidity, volatile_acidity, citric_acid ,residual_sugar ,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol = data.split(',')
    return prediction(fixed_acidity, volatile_acidity, citric_acid ,residual_sugar ,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)


@app.post("/api/predict")
async def predict():
    # generer une combinaison de donnees permettant d'identifier un vin parfait
    return {"post predict genere vin parfait"}


@app.get("/api/model")
async def get_model():
    # lire le model serialise
    return {"get model lire model serialise"}


@app.get("/api/model/prediction")
async def model_info():
    # obtenir descriptions/informations sur le model
    return {"get model/prediction info model"}


@app.put("/api/model")
async def add_wine():
    # ajout d'un vin dans le dataset
    return {"put model ajout vin"}


@app.post("/api/model/retrain")
async def retrain_model():
    # reentrainer le model
    return {"post model/retrain reentrainer le model"}





@app.get("/")
async def root():
    return {"message": "Hello World"}