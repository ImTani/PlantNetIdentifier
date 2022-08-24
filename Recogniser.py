import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing import image
import FlowerGUI as fl
from tkinter import filedialog

class_names = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

# model = tf.keras.models.load_model("modelTest")

TF_MODEL_FILE_PATH = 'model.tflite'  # The default path to the saved TensorFlow Lite model

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)

path = filedialog.askopenfilename(title="Choose An Image", filetypes=[('image files', ('.png', '.jpg'))])

img = tf.keras.utils.load_img(
    path, target_size=(180, 180)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

# result = model.predict(img_array)
# score = tf.nn.softmax(result[0])

classify_lite = interpreter.get_signature_runner('serving_default')
classify_lite

predictions_lite = classify_lite(sequential_5_input=img_array)['outputs']
score_lite = tf.nn.softmax(predictions_lite)

# assert np.allclose(result, predictions_lite)

fl.NewFrame.MakeTrivia(
    "The flower in this image is most likely a {} with a {:.2f} % confidence."
    .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite)),
    ImagePath=path)

# fl.NewFrame.MakeTrivia(
#     "This image most likely belongs to {} with a {:.2f} percent confidence."
#     .format(class_names[np.argmax(score)], 100 * np.max(score)),
#     ImagePath=path)
