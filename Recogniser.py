import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing import image
import cv2
import FlowerGUI as fl  

cnn = tf.keras.models.load_model("modelTest")
path = 'Predictions/dandelions.jpg'
cvimage = cv2.imread(path)

test_img = image.load_img(path, target_size=(64, 64))
test_img = image.img_to_array(test_img)
test_img = np.expand_dims(test_img, axis=0)
result = cnn.predict(test_img)

if result[0][0] == 1:
    res = "Daisy"
elif result[0][1] == 1:
    res = "Dandelion"
elif result[0][2] == 1:
    res = "Rose"
elif result[0][3] == 1:
    res = "Sunflower"
elif result[0][4] == 1:
    res = "Tulip"

fl.NewFrame.MakeTrivia("This image is an : ", res, path, "LolzyPOPO")
