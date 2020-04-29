from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from pydantic import BaseModel

from .ml.rowing_model import get_model, RowingModel



def check_image(name):
    ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg']
    if ('.' not in name) or (name=='') or (name.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS):
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Image attached is not allowed")
    return name


class PredictionResponse(BaseModel):
    predicted_class: str
    predicted_prob: float


app = FastAPI()

@app.get("/")
def return_usage():
    return {"Usage": "Attach image in post request to endpoint /v1/predict,\
        allowed filetypes are .jpg, .jpeg, .png"}

@app.post("/v1/predict", response_model=PredictionResponse)
def predict(image: UploadFile = File(...), model: RowingModel = Depends(get_model)):
    check_image(image.filename)
    pred_class, pred_prob = model.predict(image.file)
    return PredictionResponse(predicted_class=pred_class, predicted_prob=pred_prob)