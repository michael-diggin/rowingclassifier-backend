from fastapi import FastAPI, File, Depends
from fastapi.security.api_key import APIKey
from starlette.middleware.cors import CORSMiddleware


from api.ml.rowing_model import get_model, RowingModel
from api.datastructures import InputImage, PredictionResponse, BaseResponse
from api.security import check_api_key




app = FastAPI(
    title = "Rowing Classifier", 
    description = "A RESTful API that can predict the type of rowing boat in a given image. \n \
        Built on top of FastAPI, and uses a Tensorflow model",
    version = "0.1.0",
    docs_url = "/api/docs",
    redoc_url = "/api/redoc" 
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event('startup')
def startup_event():
    # run the get model function on startup 
    # to cache the result, only loaded from disk once
    get_model()

@app.get("/api/v1", response_model=BaseResponse)
def return_usage(api_key: APIKey = Depends(check_api_key)):
    """
    Return the API usage and allowed image types
    """
    return BaseResponse()

@app.post("/api/v1/predict", response_model=PredictionResponse, summary="Generate prediction", response_description="Predicted class type and probability")
def predict(image: InputImage = File(...), model: RowingModel = Depends(get_model), 
            api_key: APIKey = Depends(check_api_key)):
    """
    Predict the type of rowing boat in an image:

    - **image**: must be supplied in .jpg, .jpeg or .png format 
    """
    pred_class, pred_prob = model.predict(image.file)
    return PredictionResponse(ImageName=image.filename, PredictedClass=pred_class, PredictedProb=pred_prob)