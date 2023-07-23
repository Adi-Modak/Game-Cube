from tkinter import *
from Root import *
from PIL import ImageTk,Image
import Matching2
import project1
import RPS
import Hangman
import praak

def options(name):
    def Forget():
        for widget0 in f0.winfo_children():
            widget0.pack_forget()
        f0.pack_forget()
        for widget1 in f1.winfo_children():
            widget1.pack_forget()
        f1.pack_forget()
        for widget2 in f2.winfo_children():
            widget2.pack_forget()
        f2.pack_forget()
        for widget3 in f3.winfo_children():
            widget3.pack_forget()
        f3.pack_forget()


    def play1():
        Forget()
        Matching2.play()
        
    def play2():
        Forget()
        root.geometry("490x550")
        project1.play()
    def play3():
        Forget()
        root.geometry("1140x650")
        RPS.play()

    def play4():
        Hangman.main()

    def play5():
        Forget()
        praak.mygame()
    f0 = Frame(root, bg="orange")
    f0.pack(pady=10)
    f1 = Frame(root, bg="orange")
    f1.pack(pady=10)
    f2 = Frame(root, bg="orange")
    f2.pack(pady=10)
    f3 = Frame(root, bg="orange")
    f3.pack(pady=10)
    l0 = Label(f0, text="Welcome!", font=20, bg="orange")
    l0.pack(pady=10, side=LEFT)
    l1 = Label(f0, text=name, font=(20), bg="orange")
    l1.pack(pady=10,side=LEFT)
    l2 = Label(f1, text="Select Your Game", font=(20), bg="purple")
    l2.pack(pady=10)
    b1 = Button(f1, text="Matching Game", height=3, width=17, font=("Helvetica",15), command=play1, relief="groove")
    b2 = Button(f1, text="Tic Tac Toe", height=3, width=17, font=("Helvetica",15), command=play2, relief="groove")
    b3 = Button(f2, text="Rock Paper Scissor", height=3, width=17, font=("Helvetica",15), command=play3, relief="groove")
    b4 = Button(f2, text="Hangman", height=3, width=17, font=("Helvetica",15), command=play4, relief="groove")
    b5 = Button(f3, text="Street Fight", height=3, width=17, font=("Helvetica",15), command=play5, relief="groove")
    b6 = Button(f3, text="QUIT", width=10, font=("Helvetica",10), command=root.quit, relief="groove", bg="red")
    b1.pack(pady=10, side="left")
    b2.pack(pady=10, side="left")
    b3.pack(pady=10, side="left")
    b4.pack(pady=10, side="left")
    b5.pack(pady=10)
    b6.pack(pady=10, side="bottom")

    root.mainloop()

def hehehe():
    master = Toplevel() 
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