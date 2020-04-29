import os
from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename
import tempfile

from api import application, model, ALLOWED_EXTENSIONS



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
            resp = jsonify({'class': pred_class, 'probability': f"{round(prob, 2)}%",})
        else:
            resp = make_response(jsonify(
                {'error': 'Attached media not an image of the form jpg, png or jpeg'}), 400)
    else:
        resp = make_response(jsonify({'error': 'No image attached'}), 404)
    return resp




if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000, debug=True)