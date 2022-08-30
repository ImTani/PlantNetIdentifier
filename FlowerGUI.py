# import tkinter as tk
# from tkinter import filedialog
# import customtkinter as ctk
# from PIL import Image, ImageTk
# import sys
import cv2
# import pyttsx3


# FontStyle = ("Segoi UI", 12)
# class NewFrame:

#     root = ctk.CTk()
#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")
#     root.title("PushpSoochak")
#     root.geometry('1000x700')
#     guess_frame = ctk.CTkFrame(root)
#     curent_frame = guess_frame

#     def Speak(audio):
#         engine = pyttsx3.init()

#         voices = engine.getProperty('voices')

#         engine.setProperty('voice', voices[0].id)
#         engine.say(audio)
#         engine.runAndWait()

#     def ButtonExitCommand():
#         sys.exit()

#     def MakeGuess(Label1_Text: str, ImagePath: str):
#         '''Makes a Frame Window with 2 Labels and a Button.'''

#         global current_frame

#         frame.pack(padx=50, pady=70, fill="both", expand=True)
#         label = ctk.CTkLabel(frame, text=Label1_Text, text_font=FontStyle)
#         label.pack(padx=10, pady=12)
#         myImage = Image.open(ImagePath)
#         myImage1 = myImage.resize((350, 350), Image.ANTIALIAS)
#         FLimage = ImageTk.PhotoImage(image=myImage1)
#         # old_height = FLimage.height()
#         # old_width = FLimage.width()
#         # scale_w = 300 / old_width
#         # scale_h = 300 / old_height
#         # FLimage._PhotoImage__photo.zoom(scale_w, scale_h)
#         imageLabel = ctk.CTkLabel(master=frame, image=FLimage)
#         imageLabel.pack(pady=30, padx=10)
#         # label2 = ctk.CTkLabel(frame, text=BelowImage_Text)
#         # label2.pack(padx=10, pady=12)
#         button = ctk.CTkButton(master=frame, text="Exit", width=20,
#                                text_font=FontStyle, command=lambda: NewFrame.ButtonExitCommand())
#         button.pack(side="bottom", anchor="e", padx=20, pady=10)
#         button2 = ctk.CTkButton(master=frame, text="TTS", width=20,
#                                 text_font=FontStyle, command=lambda: NewFrame.Speak(Label1_Text))
#         button2.pack(side="bottom", anchor="w", padx=20, pady=10)

#  root.mainloop()

class WebcamPicture:
    def takePicture():
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("ImageClick")
        
        img_counter = 0

        while True:
            ret, frame = cam.read()
            
            cv2.imshow('ImageClick', frame)
            
            k = cv2.waitKey(1)
            
            if not ret:
                print("Couldn't grab frame.")
                break
            elif k % 256 == 27:
                #  ESC is pressed.
                break
            elif k % 256 == 32:
                image_name = "flower_image.png"
                cv2.imwrite(image_name, frame)
                img_counter += 1
                
        cam.release()
        
        cv2.destroyAllWindows()


# WebcamPicture.takePicture()
