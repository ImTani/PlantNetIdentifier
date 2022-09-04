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

TF_MODEL_FILE_PATH = 'NEWmodel.tflite'

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)

path = './flower_image.png'


# # # TEXT # # #

roseText = '''The rose is a type of flowering shrub. Its name comes from the Latin word Rosa.

There are over three hundred species and tens of thousands of cultivars. The flowers of the rose grow in many different colors, from the well-known red rose or yellow rose and sometimes white or purple rose.
Rose thorns are actually prickles - outgrowths of the epidermis.

Roses belong to the family of plants called Rosaceae. All roses were originally wild: they grew in North America, Europe, northwest Africa and many parts of Asia and Oceania. There are over 100 different species of roses. The wild rose species can be grown in gardens, but most garden roses are cultivars, which have been selected by people

Over hundreds of years they have been specially bred to produce a wide variety of growing habits and a broad range of colours from dark red to white including as well yellow and a bluish/lilac colour. Many roses have a strong, pleasant scent.

Most roses have spines (incorrectly called thorns) on their stems. This is a common defense system in plants.'''

roseTriv = '''Scientific Name : Rosa

Grows in : Open Plains with plenty of sunlight

Used as : Ornamental Plants and Perfumes

Fun Fact : Roses are edible!'''
 
# --------------

daisyTriv = '''Scientific Name : Bellis Perennis

Grows in : Anywhere! Daisies are very adaptable and can grow in almost any kind of climate!

Used as : Medicines and Food

Fun Fact : The name 'Daisy' means 'Day's Eyes!' '''

daisyText = '''Bellis Perennis is a very common European species of daisy, of the Asteraceae family, often considered the model type for the name "Daisy".

Many related plants also share the name "Daisy", so to distinguish this species from other daisies it is sometimes qualified as common daisy, lawn daisy or English daisy. The plant resembles Leucanthemum Vulgare, a similar plant in the same family. Bellis Perennis is native to western, central and northern Europe, but widely naturalised in most temperate regions including the Americas and Australasia.
It is an low herbaceous perennial plant with short rhizomes and rosettes of small rounded or spoon-shaped leaves that are 2-5 cm (0.8-2.0 in) long and grow flat to the ground.

The flower heads are 2-3 cm (0.8-1.2 in) in diameter. Although the 'flower' may appear to consist of a yellow centre with white petals, this is not the case. Each individual "petal" is itself an individual flower; these flowers are called ray flowers. In the centre (the "disk") there are also many tiny yellow flowers; these are called the disk flowers. The different colours and styles of flower work together in order to attract insects. The flower heads are produced on stems without leaves that are 2-10 cm (0.8-3.9 in) tall.'''

# --------------

sunflowerText = '''The sunflower (Helianthus annuus) is a living annual plant in the family Asteraceae, with a large flower head (capitulum). 

The stem of the flower can grow up to 3 metres tall, with a flower head that can be 30 cm wide. Other types of sunflowers include the California Royal Sunflower, which has a burgundy (red + purple) flower head.

The flower head is actually an inflorescence made of hundreds or thousands of tiny flowers called florets. The central florets look like the centre of a normal flower, apseudanthium. The benefit to the plant is that it is very easily seen by the insects and birds which pollinate it, and it produces thousands of seeds.

The sunflower is the state flower of Kansas. That is why Kansas is sometimes called the Sunflower State. To grow well, sunflowers need full sun. They grow best in fertile, wet, well-drained soil with a lot of mulch. In commercial planting, seeds are planted 45 cm (1.5 ft) apart and 2.5 cm (1 in) deep

The outer petal-bearing florets are the sterile florets and can be yellow, red, orange, or other colors. The florets inside the circular head are called disc florets, which mature into seeds.'''

sunflowerTriv = '''Scientific Name : Helianthus

Grows in : Direct Sunlight and Well-Draining Soil in Hot Summers

Used as : Yellow Dye and To Make Sunflower Oil

Fun Fact : Sunflowers always point towards the Sun! Hence, earning them the name Sunflower.'''

# --------------

dandelionText = '''A dandelion is a flower. Its scientific name is Taraxacum, a large genus of flowering plants in the family Asteraceae. Taraxacum are native to Eurasia, and have been widely introduced to North and South America and other continents. They are an invasive species in some areas. Two species, T. Officinale and T. Erythrospermum, are found as weeds worldwide. All parts of both species are edible.

Their sharp leaves look a bit like lion's teeth. Its seeds are like little parachutes that fly away with the wind, spreading and growing more dandelions. They are used in China as medicine. Dandelion pollen can often make people have allergies.

Like other members of the Asteraceae family, they have small flowers collected together into a composite flower head. Each single flower in a head is called a floret. Many Taraxacum species produce seeds asexually by apomixis, where the seeds are produced without pollination. This results in offspring that are genetically identical to the parent plant.

Al Razi around 900 (A.D.) wrote "The Tarashaquq is like chicory". A Muslim scientist and philosopher Ibn Sīnā around 1000 (A.D.) wrote a book chapter on Taraxacum. Gerard of Cremona, in translating Arabic to Japanese around 1170, spelled it Tarasacon.'''

dandelionTriv = '''Scientific Name : Taraxacum

Grows in : Any Area with Adequate Sunlight and NOT in Shade

Used as : Used as Medicine in Traditional Chinese Medicines and European Medicines

Fun Fact : Dandelion is the only flower representing three celestial bodies during different phases of its life cycle - sun, moon, stars.'''

# --------------

tulipText = '''Tulip (Tulipa) is a potflower plant. There is many cultivars and species of tulips. Cultivars are used as ornamental plants.

It grows in southern Europe, north Africa, and Asia from Anatolia and Iran in the east to northeast of China and Japan, Indo Asia. It is the national flower of Afghanistan.

There are about 75 species, and these are divided among four subgenera. The name "Tulip" is thought to be derived from a Persian word for turban, which it may have been thought to resemble by those who discovered it. Tulips originally were found in a band stretching from Southern Europe to Central Asia, but since the seventeenth century have become widely naturalised and cultivated (see map). In their natural state they are adapted to steppes and mountainous areas with temperate climates. Flowering in the spring, they become dormant in the summer once the flowers and leaves die back, emerging above ground as a shoot from the underground bulb in early spring.

Breeding programmes have produced thousands of hybrid and cultivars in addition to the original species (known in horticulture as botanical tulips). They are popular throughout the world, both as ornamental garden plants and as cut flowers.'''

tulipTriv = '''Scientific Name : Tulipa

Grows in : Shady Areas Without a Lot of Heat and Well-Drained Soil

Used as : To Make Wine and Food

Fun Fact : Tulips used to be the currency of The Netherlands at one point in time!'''

# # # GUI # # #

FontStyle = ("Segoi UI Light", 12)
FontStyleText = ("Segoi UI", 18)
FontStyleBig = ("Segoi UI Bold", 24)

def Speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def ButtonExitCommand():
    sys.exit()

def ShowGuess():
    global current_frame
    current_frame.grid_forget()
    guess_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=80, pady=24)
    guess_frame.columnconfigure(0, weight=1)
    guess_frame.columnconfigure(1, weight=1)
    guess_frame.columnconfigure(2, weight=1)
    guess_frame.rowconfigure(0, weight=1)
    guess_frame.rowconfigure(3, weight=1)
    current_frame = guess_frame

def ShowMain():
    global current_frame
    current_frame.grid_forget()
    main_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=300, pady=100)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    current_frame = main_frame

def ShowRose():
    global current_frame
    current_frame.grid_forget()
    rose_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=60, pady=24)
    rose_frame.columnconfigure(0, weight=1)
    rose_frame.rowconfigure(0, weight=1)
    current_frame = rose_frame

def ShowDaisy():
    global current_frame
    current_frame.grid_forget()
    daisy_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=60, pady=24)
    daisy_frame.columnconfigure(0, weight=1)
    daisy_frame.rowconfigure(0, weight=1)
    current_frame = daisy_frame

def ShowSunflower():
    global current_frame
    current_frame.grid_forget()
    sunflower_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=60, pady=24)
    sunflower_frame.columnconfigure(0, weight=1)
    sunflower_frame.rowconfigure(0, weight=1)
    current_frame = sunflower_frame

def ShowDandelion():    
    global current_frame
    current_frame.grid_forget()
    dandelion_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=60, pady=24)
    dandelion_frame.columnconfigure(0, weight=1)
    dandelion_frame.rowconfigure(0, weight=1)
    current_frame = dandelion_frame

def ShowTulip():
    global current_frame
    current_frame.grid_forget()
    tulip_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=60, pady=24)
    tulip_frame.columnconfigure(0, weight=1)
    tulip_frame.rowconfigure(0, weight=1)
    current_frame = tulip_frame

def MakeRose():
    img = Image.open("./Predictions/rose.jpg")
    img1 = img.resize((200, 290), Image.Resampling.LANCZOS)
    RoseImage = ImageTk.PhotoImage(image=img1)
    imgLabel = ctk.CTkLabel(master=rose_frame, image=RoseImage)
    imgLabel.image = RoseImage
    imgLabel.grid(row=1, column=0, padx=15, pady=20, sticky=tk.W)
    
    nameLabel = ctk.CTkLabel(rose_frame, text="Rose", text_font=FontStyleBig)
    nameLabel.grid(row=0, column=0, padx=10, pady=20, sticky=tk.W)
    
    TrivText = ctk.CTkTextbox(master=rose_frame, height=150, width=850, text_font=FontStyle, wrap='word')
    TrivText.insert(tk.END, roseTriv)
    TrivText.grid(row=0, column=2, padx=10, pady=20)
    
    desLabel = ctk.CTkTextbox(master=rose_frame, height=300, width=850, text_font=FontStyle, wrap='word')
    desLabel.insert(tk.END, roseText)
    desLabel.grid(row=1, column=2, padx=10, pady=10)

    button = ctk.CTkButton(master=rose_frame, text="Exit", width=20,
                           text_font=FontStyle, command=lambda: ButtonExitCommand())
    button.grid(row=2, column=2, sticky=tk.SE, padx=20, pady=20)
    
    button2 = ctk.CTkButton(master=rose_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(roseText))
    button2.grid(row=2, column=0, sticky=tk.SW, padx=20, pady=20)

def MakeSunflower():
    img = Image.open("./Predictions/sunflowers1.jpg")
    img1 = img.resize((240, 320), Image.Resampling.LANCZOS)
    sunflowerImage = ImageTk.PhotoImage(image=img1)
    imgLabel = ctk.CTkLabel(master=sunflower_frame, image=sunflowerImage)
    imgLabel.image = sunflowerImage
    imgLabel.grid(row=1, column=0, padx=15, pady=20, sticky=tk.W)
    
    nameLabel = ctk.CTkLabel(sunflower_frame, text="Sunflower", text_font=FontStyleBig)
    nameLabel.grid(row=0, column=0, padx=10, pady=20, sticky=tk.W)
    
    TrivText = ctk.CTkTextbox(master=sunflower_frame, height=150, width=850, text_font=FontStyle, wrap='word')
    TrivText.insert(tk.END, sunflowerTriv)
    TrivText.grid(row=0, column=2, padx=10, pady=20)
    
    desLabel = ctk.CTkTextbox(master=sunflower_frame, height=300, width=850, text_font=FontStyle, wrap='word')
    desLabel.insert(tk.END, sunflowerText)
    desLabel.grid(row=1, column=2, padx=10, pady=10)
    
    button = ctk.CTkButton(master=sunflower_frame, text="Exit", width=20,
                           text_font=FontStyle, command=lambda: ButtonExitCommand())
    button.grid(row=2, column=2, sticky=tk.SE, padx=20, pady=20)

    button2 = ctk.CTkButton(master=sunflower_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(sunflowerText))
    button2.grid(row=2, column=0, sticky=tk.SW, padx=20, pady=20)

def MakeTulip():
    img = Image.open("./Predictions/tulips.jpg")
    img1 = img.resize((300, 220), Image.Resampling.LANCZOS)
    tulipImage = ImageTk.PhotoImage(image=img1)
    imgLabel = ctk.CTkLabel(master=tulip_frame, image=tulipImage)
    imgLabel.image = tulipImage
    imgLabel.grid(row=1, column=0, padx=15, pady=20, sticky=tk.W)
    
    nameLabel = ctk.CTkLabel(tulip_frame, text="Tulip", text_font=FontStyleBig)
    nameLabel.grid(row=0, column=0, padx=10, pady=20, sticky=tk.W)
    
    TrivText = ctk.CTkTextbox(master=tulip_frame, height=150, width=850, text_font=FontStyle, wrap='word')
    TrivText.insert(tk.END, tulipTriv)
    TrivText.grid(row=0, column=2, padx=10, pady=20)
    
    desLabel = ctk.CTkTextbox(master=tulip_frame, height=300, width=850, text_font=FontStyle, wrap='word')
    desLabel.insert(tk.END, tulipText)
    desLabel.grid(row=1, column=2, padx=10, pady=10)
    
    button = ctk.CTkButton(master=tulip_frame, text="Exit", width=20,
                           text_font=FontStyle, command=lambda: ButtonExitCommand())
    button.grid(row=2, column=2, sticky=tk.SE, padx=20, pady=20)
    
    button2 = ctk.CTkButton(master=tulip_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(tulipText))
    button2.grid(row=2, column=0, sticky=tk.SW, padx=20, pady=20)

def MakeDandelion():
    img = Image.open("./Predictions/DandelionFlower.jpg")
    img1 = img.resize((294, 236), Image.Resampling.LANCZOS)
    dandelionImage = ImageTk.PhotoImage(image=img1)
    imgLabel = ctk.CTkLabel(master=dandelion_frame, image=dandelionImage)
    imgLabel.image = dandelionImage
    imgLabel.grid(row=1, column=0, padx=15, pady=20, sticky=tk.W)
    
    nameLabel = ctk.CTkLabel(dandelion_frame, text="Dandelion", text_font=FontStyleBig)
    nameLabel.grid(row=0, column=0, padx=10, pady=20, sticky=tk.W)
    
    TrivText = ctk.CTkTextbox(master=dandelion_frame, height=170, width=850, text_font=FontStyle, wrap='word')
    TrivText.insert(tk.END, dandelionTriv)
    TrivText.grid(row=0, column=2, padx=10, pady=20)
    
    desLabel = ctk.CTkTextbox(master=dandelion_frame, height=300, width=850, text_font=FontStyle, wrap='word')
    desLabel.insert(tk.END, dandelionText)
    desLabel.grid(row=1, column=2, padx=10, pady=10)
    
    button = ctk.CTkButton(master=dandelion_frame, text="Exit", width=20,
                           text_font=FontStyle, command=lambda: ButtonExitCommand())
    button.grid(row=2, column=2, sticky=tk.SE, padx=20, pady=20)
    
    button2 = ctk.CTkButton(master=dandelion_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(dandelionText))
    button2.grid(row=2, column=0, sticky=tk.SW, padx=20, pady=20)

def MakeDaisy():
    img = Image.open("./Predictions/daisies.jpg")
    img1 = img.resize((300, 300), Image.Resampling.LANCZOS)
    DaisyImage = ImageTk.PhotoImage(image=img1)
    imgLabel = ctk.CTkLabel(master=daisy_frame, image=DaisyImage)
    imgLabel.image = DaisyImage
    imgLabel.grid(row=1, column=0, padx=15, pady=20, sticky=tk.W)
    
    nameLabel = ctk.CTkLabel(daisy_frame, text="Daisy", text_font=FontStyleBig)
    nameLabel.grid(row=0, column=0, padx=10, pady=20, sticky=tk.W)
    
    TrivText = ctk.CTkTextbox(master=daisy_frame, height=150, width=850, text_font=FontStyle, wrap='word')
    TrivText.insert(tk.END, daisyTriv)
    TrivText.grid(row=0, column=2, padx=10, pady=20)
    
    desLabel = ctk.CTkTextbox(master=daisy_frame, height=300, width=850, text_font=FontStyle, wrap='word')
    desLabel.insert(tk.END, daisyText)
    desLabel.grid(row=1, column=2, padx=10, pady=10)
    
    button = ctk.CTkButton(master=daisy_frame, text="Exit", width=20,
                           text_font=FontStyle, command=lambda: ButtonExitCommand())
    button.grid(row=2, column=2, sticky=tk.SE, padx=20, pady=20)
    
    button2 = ctk.CTkButton(master=daisy_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(daisyText))
    button2.grid(row=2, column=0, sticky=tk.SW, padx=20, pady=20)

def MakeGuess(Label1_Text: str, ImagePath: str):
        
    label = ctk.CTkLabel(guess_frame, text=Label1_Text, text_font=FontStyleText)
    # label.pack(padx=10, pady=12)
    label.grid(row=0, column=1, pady=40, sticky=tk.N)                  
    
    myImage = Image.open(ImagePath)
    
    if myImage:
        print("Image gathered")
    
    myImage1 = myImage.resize((400, 400), Image.Resampling.LANCZOS)
    FLimage = ImageTk.PhotoImage(image=myImage1)
    imageLabel = ctk.CTkLabel(master=guess_frame, image=FLimage)
    imageLabel.image = FLimage
    
    # imageLabel.pack(pady=30, padx=10)
    
    imageLabel.grid(row=1, column=1, pady=20)
    
    button = ctk.CTkButton(master=guess_frame, text="Next", width=20,
                           text_font=FontStyle, command=lambda: ChangeFrames())
    # button.pack(side="bottom", anchor="e", padx=20, pady=10)
    button.grid(row=4, column=2, sticky=tk.SE, padx=20, pady=20)
    
    button2 = ctk.CTkButton(master=guess_frame, text="Speak", width=20,
                            text_font=FontStyle, command=lambda: Speak(Label1_Text))
    # button2.pack(side="bottom", anchor="w", padx=20)
    button2.grid(row=4, column=0, sticky=tk.SW, padx=20, pady=20)
    
def MakeMain():
    
    label1 = ctk.CTkLabel(main_frame, text="PlantNet Identification", text_font=FontStyleBig)
    label1.grid(row=0, column=0, pady=20)
    
    button1 = ctk.CTkButton(master=main_frame, text="Start", width=60,
                            text_font=FontStyleBig, command=lambda: ShowGuess())
    button1.grid(row=1, column=0, pady=10)
    
    label2 = ctk.CTkLabel(main_frame, text="Made by : Tanishk Narula", text_font=FontStyle)
    label2.grid(row=2, column=0, pady=20, padx=20, sticky=tk.SE)

def ChangeFrames():
    if class_names[np.argmax(score_lite)] == "Rose":
        ShowRose()
    if class_names[np.argmax(score_lite)] == "Daisy":
        ShowDaisy()
    if class_names[np.argmax(score_lite)] == "Dandelion":
        ShowDandelion()
    if class_names[np.argmax(score_lite)] == "Sunflower":
        ShowSunflower()
    if class_names[np.argmax(score_lite)] == "Tulip":
        ShowTulip()
        

def PredictStuff():
    
    global path
    
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

    prediction_res = "The flower in this image is most likely a {} with a {:.2f}% confidence.".format(
        class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
    
    return prediction_res, score_lite


root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root.title("PlantNet Identification")
root.geometry('1000x700')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

bg = ImageTk.PhotoImage(file='./Predictions/Background.png')
canv = ctk.CTkCanvas(root, width=1366, height=768)
canv.grid(row=0, column=0, sticky=tk.NW)
canv.create_image(0, 0, image=bg, anchor='nw')

main_frame = ctk.CTkFrame(root)
main_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=24, pady=48)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

guess_frame = ctk.CTkFrame(root)

rose_frame = ctk.CTkFrame(root)
dandelion_frame = ctk.CTkFrame(root)
sunflower_frame = ctk.CTkFrame(root)
daisy_frame = ctk.CTkFrame(root)
tulip_frame = ctk.CTkFrame(root)

current_frame = main_frame

# # # RUNNING EVERYTHING # # #

MakeRose()
MakeDaisy()
MakeDandelion()
MakeSunflower()
MakeTulip()
MakeMain()
fl.WebcamPicture.takePicture()
prediction_res, score_lite = PredictStuff()
MakeGuess(prediction_res, ImagePath=path)

root.state('zoomed')

root.mainloop()
