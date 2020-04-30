import pytest
import numpy as np
from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_400_BAD_REQUEST


def test_predict(test_client: TestClient):
    np.random.seed(0)
    test_image = 'default_eight_image.jpg'
    files = {'image': open(test_image, 'rb')}
    resp = test_client.post("/api/v1/predict", files=files)
    assert resp.status_code == HTTP_200_OK
    assert resp.json()['PredictedClass'] == 'Eights'
    assert round(resp.json()['PredictedProb'], 4) == 0.5928
    assert resp.json()['ImageName'] == test_image

def test_predict_with_wrong_input(test_client: TestClient):
    files = {'image': open('__init__.py', 'rb')}
    resp = test_client.post("/api/v1/predict", files=files)
    assert resp.status_code == HTTP_422_UNPROCESSABLE_ENTITY

def test_with_no_input(test_client: TestClient):
    files = {'image': None}
    resp = test_client.post("/api/v1/predict", files=files)
    assert resp.status_code == HTTP_400_BAD_REQUEST