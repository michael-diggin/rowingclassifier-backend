import pytest
from starlette.testclient import TestClient

from ..main import app
from ..ml.rowing_model import get_model
from .mocks import MockModel


def get_model_override():
    return MockModel()

app.dependency_overrides[get_model] = get_model_override

@pytest.fixture()
def test_client():
    return TestClient(app)