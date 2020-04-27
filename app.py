import os
from flask import Flask, request, jsonify, make_response
from werkzeug.utils import secure_filename
import tempfile

from rowing_api.rowing_model import RowingModel


UPLOAD_FOLDER = tempfile.mkdtemp()
ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_SIZE'] = 16*1024*1024

model = RowingModel()


def allowed_file(filename):
    return ('.' in filename) and (filename!='') and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route('/v1/predict', methods=['GET', 'POST'])
def file_upload():
    if request.files:
        image = request.files['image']
        if allowed_file(image.filename):
            filename = secure_filename(image.filename)
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(img_path)
            pred_class, prob = model.predict(img_path)
            resp = jsonify({'class': pred_class, 'probability': f"{round(prob, 2)}%"})
        else:
            resp = make_response(jsonify(
                {'error': 'Attached media not an image of the form jpg, png or jpeg'}), 400)
    else:
        resp = make_response(jsonify({'error': 'No image attached'}), 404)
    return resp




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)