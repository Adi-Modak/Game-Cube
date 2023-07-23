from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.geometry("978x550")
root.title("Game Cube")
photo = ImageTk.PhotoImage(Image.open("logo.png"))
root.iconphoto(False, photo)
root.configure(bg="orange")