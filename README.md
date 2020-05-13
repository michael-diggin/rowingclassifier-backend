[![Build Status](https://travis-ci.org/michael-diggin/rowingclassifier-backend.svg?branch=master)](https://travis-ci.org/michael-diggin/rowingclassifier-backend)

# Rowing Classifier
Rowing Classifier is a web page that classifies the type of rowing boat in a user uploaded image. 

This repository contains backend source code, built using Python and on top of the [FastAPI](https://fastapi.tiangolo.com/) framework. The frontend source code can be found at [this repo](https://github.com/michael-diggin/rowingclassifier-frontend).  

The underlying deep learning model was built and trained using Tensorflow and can be found [here](https://github.com/mdiggin/rowing-classifier). It uses transfer learning and is based on top of the VGG16 model. 
