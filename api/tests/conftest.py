import pytest
from starlette.testclient import TestClient

from api.main import app
from api.ml.rowing_model import get_model
from api.security import check_api_key
from api.tests.mocks import MockModel, TestModel


def get_model_override():
    return MockModel()

def get_api_key_override():
    return

app.dependency_overrides[get_model] = get_model_override
app.dependency_overrides[check_api_key] = get_api_key_override

@pytest.fixture()
def test_client():
    return TestClient(app)

@pytest.fixture()
def test_model():
    return TestModel('model_path')