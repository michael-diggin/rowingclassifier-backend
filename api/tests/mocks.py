import numpy as np

class MockModel:
    def predict(self, img):
        pred_class = np.random.choice(['Eights', 'Doubles', 'Singles'])
        pred_prob = np.random.rand()
        return pred_class, pred_prob