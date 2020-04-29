import os
import tensorflow as tf
import numpy as np
from pathlib import Path


class RowingModel():
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        model_path = 'saved_models/model_with_preprocess.h5'
        model = tf.keras.models.load_model(self.model_path)
        return model

    def _preprocess_img(self, img):
        img = tf.keras.preprocessing.image.load_img(img, target_size=(224, 224))
        img_tensor = tf.keras.preprocessing.image.img_to_array(img)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        img_tensor = img_tensor/255.
        return img_tensor

    def _map_pred_to_class(self, array):
        l = list(array[0])
        classes = ['Doubles', 'Eights','Fours', 'Pairs', 'Quads', 'Singles']
        index = l.index(max(l))
        return classes[index], max(l)

    def predict(self, image):
        img_tensor = self._preprocess_img(image)
        model_pred = self.model.predict(img_tensor)
        pred_class, prob = self._map_pred_to_class(model_pred)
        return pred_class, prob*100

model_path = os.path.join(Path(__file__).parent, 'saved_models/model_with_preprocess.h5')
rowing_model = RowingModel(model_path)

def get_model():
    return rowing_model