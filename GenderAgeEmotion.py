from flask import Flask, request, jsonify, url_for, render_template
import uuid
import os
from tensorflow.keras.models import load_model
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.applications import MobileNet
from PIL import Image, ImageFile
from io import BytesIO
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications.mobilenet import decode_predictions
import pickle
from deepface import DeepFace
import matplotlib.pyplot as plt
import pandas as pd



ALLOWED_EXTENSION = set(['pdf', 'png', 'jpg', 'jpeg'])



def allowed_file(filename):
    return '.' in filename and \
     filename.rsplit('.',1)[1] in ALLOWED_EXTENSION

img1_path = 'Swapnil.jpg'
img2_path = 'tests/datasets/img3.jpg'

app = Flask(__name__)

model = MobileNet(weights='imagenet', include_top=True)
model_name = 'ArcFace'
resp = DeepFace.verify(img1_path = img1_path,img2_path = img2_path, model_name = model_name)
df = DeepFace.find(img_path = 'source.jpg',db_path = 'tests/datasets' )


@app.route('/')

def index():
    return render_template('ImageML.html')



@app.route('/result', methods=['POST'])

def upload_image():
    
    if 'image' not in request.files:
        
        return render_template('ImageML.html', prediction='No image found')
    
    file = request.files['image']
    
    if file.filename =='':
        
        return render_template('ImageML.html', prediction='Selected NO Image')
    
    if file and allowed_file(file.filename):
        
        filename = secure_filename(file.filename)
        
        print("*"+filename)
        
        ''' Image pre-processing '''
        
        x = []
        
        ImageFile.LOAD_TRUNCATED_IMAGES = False
        
        img = Image.open(BytesIO(file.read()))
        result = DeepFace.analyze(filename)
       
        
        return render_template('ImageML.html', prediction = 'I would say the image is most likely {}'.format(result))
    else:
        return render_template('ImageML.html', prediction = 'Invalid File extension')
    
if __name__=='__main__':
    
    app.run(debug=True, use_reloader=False)
