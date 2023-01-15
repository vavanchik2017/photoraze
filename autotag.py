import tensorflow as tf
from tensorflow import keras
from keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.utils import load_img, img_to_array
import numpy as np


class VGG:

    def __init__(self):
        self.model = VGG19(weights='imagenet', include_top=True)
        self.count = 10

    def predict(self, img_path):
        img = load_img(img_path, target_size=(224, 224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = self.model.predict(x)
        return decode_predictions(preds, self.count)[0][0:5]

    def gettag(self, img_path):
        tags = self.predict(img_path)
        result = [tags[c][1] for c in range(0, 5)]
        return ', '.join(result)
