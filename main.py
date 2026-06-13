from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = None
vectorizer = None

@app.on_event("startup")
def load_model():
    global model
    global vectorizer
    model = joblib.load("svmmodel.pkl")
    vectorizer = joblib.load("vectorizer.pkl")



class EmailRequest(BaseModel):
    text:str

@app.get("/")
def home():
    return {"message":"Hello World"}

@app.post("/predict")
def predict(data:EmailRequest):
    text = data.text
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    if prediction == 1:
        prediction = "Spam"
    else:
        prediction = "Not Spam"
    return{
        "email": text,
        "prediction": str(prediction)
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)