from Test import input_prep
from tensorflow import keras
import numpy
import os
from hiragana import hiragana_classes
from katakana import katakana_classes
from keras.models import Sequential

# classes = hiragana_classes.hiragana_literals
classes = katakana_classes.katakana_literals
def test_model(model_str, image_directory, image_dims, channel):
    model = load_compile(model_str)
    x, y = input_prep.prepare_data(image_directory, image_dims, channel)
    predictions = []
    num = numpy.argmax(model.predict(x), axis=-1)
    for i in model.predict_classes(x):
        prob = model.predict_proba(x)
        predictions.append(classes[i])
    print(numpy.count_nonzero(num == numpy.reshape(y, y.size)) / y.size)
    print(predictions)
    # print("Predictions: " + num)
    # print("Actual ans : " + y)

def load_compile(path) -> Sequential:
    model = keras.models.load_model(os.path.join(os.getcwd(), path))
    return model
