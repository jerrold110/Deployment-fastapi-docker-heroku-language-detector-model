import joblib
from pathlib import Path
import os
import dill # 0.3.6
import re

# folder structure in docker may be different
BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(f'{BASE_DIR}/model/trained_pipeline.joblib', 'rb') as f:
    model = dill.load(f)
    
classes = ['Arabic', 'Danish', 'Dutch', 'English', 'French', 'German',
       'Greek', 'Hindi', 'Italian', 'Kannada', 'Malayalam', 'Portugeese',
       'Russian', 'Spanish', 'Sweedish', 'Tamil', 'Turkish']


def predict_pipeline(text):
    pred = model.predict([text])
    return classes[pred[0]]