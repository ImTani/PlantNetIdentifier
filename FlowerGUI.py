import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sys

FontStyle = ("Segoi UI", 12)
class NewFrame:

    def ButtonExitCommand():
        sys.exit()

    def MakeTrivia(Label1_Text: str, Label2_Text: str, ImagePath: str):
        '''Makes a Frame Window with 2 Labels and a Button.'''

        root = ctk.CTk()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        root.title("FlowerGUI")
        root.geometry('1000x700')
        frame = ctk.CTkFrame(root)
        frame.pack(padx=50, pady=70, fill="both", expand=True)
        label = ctk.CTkLabel(frame, text=Label1_Text + Label2_Text, text_font=FontStyle)
        label.pack(padx=10, pady=12)
        # label2 = ctk.CTkLabel(frame, text=Label2_Text)
        # label2.pack(padx=10, pady=12)
        FLimage = ImageTk.PhotoImage(Image.open(ImagePath))
        imageLabel = ctk.CTkLabel(master=frame, image=FLimage)
        imageLabel.pack(pady=30, padx=10)
        button = ctk.CTkButton(master=frame, text="Exit", width=20,
                               text_font=FontStyle, command=lambda: NewFrame.ButtonExitCommand())
        button.pack(side="bottom", anchor="e", padx=20, pady=10)
        root.mainloop()
