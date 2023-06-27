import joblib
from pathlib import Path
import os
import dill
import re # necessary for functiontransformer

__version__ = "0.1.0"

# folder structure in docker may be different
BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(f'{BASE_DIR}/trained_pipeline-{__version__}.joblib', 'rb') as f:
    model = dill.load(f)
    
classes = ['Arabic', 'Danish', 'Dutch', 'English', 'French', 'German',
       'Greek', 'Hindi', 'Italian', 'Kannada', 'Malayalam', 'Portugeese',
       'Russian', 'Spanish', 'Sweedish', 'Tamil', 'Turkish']


# data input and output is a single dimension array
def predict_pipeline(text):
    pred = model.predict([text])
    return classes[pred[0]]