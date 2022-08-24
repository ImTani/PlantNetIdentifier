import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing import image
import FlowerGUI as fl

class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

model = tf.keras.models.load_model("modelTest")
path = "Predictions/surajmukhi.jpg"

img = tf.keras.utils.load_img(
    path, target_size=(180, 180)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

result = model.predict(img_array)
score = tf.nn.softmax(result[0])

fl.NewFrame.MakeTrivia(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)),
    ImagePath=path)
