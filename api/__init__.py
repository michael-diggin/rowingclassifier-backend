from flask import Flask
from flask_cors import CORS
import tempfile
from api.rowing_model import RowingModel

UPLOAD_FOLDER = tempfile.mkdtemp()
ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg']

application = Flask(__name__)
CORS(application)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['MAX_CONTENT_SIZE'] = 16*1024*1024

model = RowingModel()

import api.app