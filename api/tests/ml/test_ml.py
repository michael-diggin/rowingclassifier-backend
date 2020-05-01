import numpy as np
from mock import patch, Mock

from api.ml import rowing_model

@patch.object(rowing_model.RowingModel, 'load_model')
def test_cache_get_model_loads_model_only_once(mock_load: Mock):
    rowing_model.get_model.cache_clear()
    [rowing_model.get_model() for _ in range(3)]
    assert mock_load.call_count == 1

def test_model_map_preds_to_class(test_model):
    test_model._preprocess_img = Mock(return_value=Mock())
    pred_class, pred_prob = test_model.predict('image')
    assert pred_class == 'Doubles'
    assert pred_prob == 90.00

def test_model_preprocess_image(test_model):
    image = 'default_eight_image.jpg'
    processed_image = test_model._preprocess_img(image)
    assert processed_image.shape == (1, 224, 224, 3)
    assert np.amin(processed_image) == 0.0
    assert np.amax(processed_image) == 1.0
