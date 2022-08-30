from PIL import Image, ImageTk
import tkinter as tk

rot = tk.Tk()

ImagePath = "./flower_image.png"

myImage = Image.open(ImagePath)
if myImage:
    print("Image gathered")
myImage1 = myImage.resize((400, 400), Image.Resampling.LANCZOS)
FLimage = ImageTk.PhotoImage(myImage1)


frame1 = tk.Frame(master=rot)
frame1.pack(padx=20, pady=20)

label1 = tk.Label(master=frame1, image=FLimage)
label1.pack(padx=10, pady=20)

rot.mainloop()
