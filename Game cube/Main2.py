from tkinter import *
from PIL import ImageTk,Image

def hehehe():
    master = Tk() 
    photo = ImageTk.PhotoImage(Image.open("logo.png"))
    master.iconphoto(False, photo)
    master.geometry("978x550")
    global my_canvas
    name = ""
    bg = ImageTk.PhotoImage(Image.open("Main2.jpg"))
    my_canvas = Canvas(master, width=550, height=550)
    my_canvas.pack(fill="both",expand=True)
    my_canvas.create_image(0,0, image=bg, anchor="nw")

    def run_options():
        name = entry1.get()
        master.destroy()
        options(name)
     
    large_font = ("Verdana",15)
    entry1 = Entry(master, width=15, font=large_font)
    my_canvas.create_window(489, 125, window=entry1)
    
    my_canvas.create_text(489, 160, text="Enter Your Name", font=("Helvetica",20), fill="yellow")
    button1 = Button(master, text="Enter Game", height=2, width=15, bg="green", font=("Helvetica",10), command=run_options)
    button1_window = my_canvas.create_window(489, 360, window=button1)
    master.mainloop()
hehehe()