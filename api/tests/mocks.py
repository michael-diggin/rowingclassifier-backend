import numpy as np
from mock import Mock

from api.ml.rowing_model import RowingModel

class MockModel:
    def predict(self, img):
        pred_class = np.random.choice(['Eights', 'Doubles', 'Singles'])
        pred_prob = np.random.rand()
        return pred_class, pred_prob

class TestModel(RowingModel):
    def load_model(self):
        model = Mock()
        model.predict.return_value = np.array([[.9, 0.1, 0., 0., 0., 0.]])
        return model