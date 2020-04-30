from fastapi import UploadFile, HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_406_NOT_ACCEPTABLE
from starlette.datastructures import UploadFile as StarletteUploadFile
from pydantic import BaseModel
from typing import Type, Any

class InputImage(UploadFile):
    ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg']

    @classmethod
    def validate(cls: Type["UploadFile"], v: Any) -> Any:
        if not isinstance(v, StarletteUploadFile):
            raise HTTPException(status=HTTP_406_NOT_ACCEPTABLE, detail=f"Expected UploadFile, received: {type(v)}")
        InputImage.check_image(v.filename)
        return v

    @staticmethod
    def check_image(name: str):
        if ('.' not in name) or (name=='') or (name.rsplit('.', 1)[1].lower() not in InputImage.ALLOWED_EXTENSIONS):
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Image attached is not allowed")
        return name

class PredictionResponse(BaseModel):
    ImageName: str
    PredictedClass: str
    PredictedProb: float

class BaseResponse(BaseModel):
    Usage: str = "Attach image in post request to endpoint /api/v1/predict"
    AllowedTypes: str = ".jpg, .jpeg, .png"
