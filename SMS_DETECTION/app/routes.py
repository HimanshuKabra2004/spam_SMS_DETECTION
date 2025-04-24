from fastapi import APIRouter
from pydantic import BaseModel
from app.predictor import predict_spam  

router = APIRouter()

class SMSInput(BaseModel):
    message: str

@router.post("/predict")
async def classify_sms(sms: SMSInput):
    result = predict_spam(sms.message)
    return {"prediction": result}
