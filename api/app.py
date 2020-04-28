import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import tempfile

from api.rowing_model import RowingModel


UPLOAD_FOLDER = '..\web\images'
ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg']

application = Flask(__name__)
CORS(application)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['MAX_CONTENT_SIZE'] = 16*1024*1024

model = RowingModel()


def allowed_file(filename):
    return ('.' in filename) and (filename!='') and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@application.route('/v1/predict', methods=['GET', 'POST'])
def file_upload():
    if request.files:
        image =request.files['image']
        if allowed_file(image.filename):
            filename = secure_filename(image.filename)
            img_path = os.path.join(application.config["UPLOAD_FOLDER"], image.filename)
            image.save(img_path)
            pred_class, prob = model.predict(img_path)
            resp = jsonify({'class': pred_class, 'probability': f"{round(prob, 2)}%", 'path': img_path})
        else:
            resp = make_response(jsonify(
                {'error': 'Attached media not an image of the form jpg, png or jpeg'}), 400)
    else:
        resp = make_response(jsonify({'error': 'No image attached'}), 404)
    return resp




if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000, debug=True)