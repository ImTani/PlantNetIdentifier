import numpy as np
import tensorflow as tf
from tensorflow import keras
import FlowerGUI as fl
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sys
import pyttsx3

class_names = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

# model = tf.keras.models.load_model("modelTest")

TF_MODEL_FILE_PATH = 'NEWmodel.tflite'  # The default path to the saved TensorFlow Lite model

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)


fl.WebcamPicture.takePicture()

path = './flower_image.png'

if path == '':
    quit()

img = tf.keras.utils.load_img(
    path, target_size=(180, 180)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

# result = model.predict(img_array)
# score = tf.nn.softmax(result[0])

classify_lite = interpreter.get_signature_runner('serving_default')
classify_lite

predictions_lite = classify_lite(sequential_input=img_array)['outputs']
score_lite = tf.nn.softmax(predictions_lite)

# assert np.allclose(result, predictions_lite)

prediction_res = "The flower in this image is most likely a {} with a {:.2f}% confidence.".format(class_names[
    np.argmax(score_lite)], 100 * np.max(score_lite))


# fl.NewFrame.MakeTrivia(
#     "This image most likely belongs to {} with a {:.2f} percent confidence."
#     .format(class_names[np.argmax(score)], 100 * np.max(score)),
#     ImagePath=path)


# # # GUI # # #

FontStyle = ("Segoi UI", 12)

def Speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def ButtonExitCommand():
    sys.exit()

def MakeGuess(Label1_Text: str, ImagePath: str):
    '''Makes a Frame Window with 2 Labels and a Button.'''

    global root

    label = ctk.CTkLabel(guess_frame, text=Label1_Text, text_font=FontStyle)
    # label.pack(padx=10, pady=12)
    label.grid(row=0, column=1, pady=20, sticky=tk.N)
    
    myImage = Image.open(ImagePath)
    
    if myImage:
        print("Image gathered")
    
    myImage1 = myImage.resize((400, 400), Image.Resampling.LANCZOS)
    FLimage = ImageTk.PhotoImage(image=myImage1)
    imageLabel = ctk.CTkLabel(master=guess_frame, image=FLimage)
    imageLabel.image = FLimage
    
    # imageLabel.pack(pady=30, padx=10)
    
    imageLabel.grid(row=1, column=1, pady=20)
    
    button = ctk.CTkButton(master=guess_frame, text="Exit", width=20,
                           text_font=FontStyle, command=lambda: ButtonExitCommand())
    # button.pack(side="bottom", anchor="e", padx=20, pady=10)
    button.grid(row=4, column=2, sticky=tk.SE, padx=20, pady=20)
    
    button2 = ctk.CTkButton(master=guess_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(Label1_Text))
    # button2.pack(side="bottom", anchor="w", padx=20)
    button2.grid(row=4, column=0, sticky=tk.SW, padx=20, pady=20)


root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.title("PlantNetIdentification")
root.geometry('1000x700')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

guess_frame = ctk.CTkFrame(root)
guess_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=12, pady=24)
guess_frame.columnconfigure(0, weight=1)
guess_frame.columnconfigure(1, weight=1)
guess_frame.columnconfigure(2, weight=1)
guess_frame.rowconfigure(0, weight=1)
guess_frame.rowconfigure(3, weight=1)

current_frame = guess_frame

# # # RUNNING EVERYTHING # # #

MakeGuess(prediction_res, ImagePath=path)
root.mainloop()
