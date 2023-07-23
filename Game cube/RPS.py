from tkinter import *
from Root import *
from PIL import ImageTk,Image
import random


def play():
  root.title('Rock Paper Scissors')
  click=True
  r_frame1 = Frame(root, bg="orange")
  r_frame1.pack(pady=10)
  r_label1 = Label(r_frame1,text="Rock,Paper,Scissors",font=("corbel",20),bg="red")
  r_label1.pack(pady=10)
  r_label2 = Label(r_frame1,text="Click one: ",font=("arial",15), bg="orange")
  r_label2.pack(pady=10)
  r_label3 = Label(r_frame1,text="      ", bg="orange")
  r_label3.pack()

  rhandPhoto=ImageTk.PhotoImage(Image.open("rhand.jpg"))
  phandPhoto=ImageTk.PhotoImage(Image.open("phand.jpg"))
  shandPhoto=ImageTk.PhotoImage(Image.open("shand.jpg"))

  rockPhoto=ImageTk.PhotoImage(Image.open("rock.jpg"))
  paperPhoto=ImageTk.PhotoImage(Image.open("paper.jpg"))
  scissorPhoto=ImageTk.PhotoImage(Image.open("scissor.jpg"))

  winnerPhoto=ImageTk.PhotoImage(Image.open("winner.jpg"))
  loosePhoto=ImageTk.PhotoImage(Image.open("loose.jpg"))
  tiePhoto=ImageTk.PhotoImage(Image.open("tie.jpg"))


  def playgame():
    global rhandButton,phandButton,shandButton
    r_frame2 = Frame(root, bg="orange")
    r_frame2.pack(pady=10)
    rhandButton=Button(r_frame2,image=rhandPhoto,command=lambda: youPick('rock'),relief="groove",padx=10)
    phandButton=Button(r_frame2,image=phandPhoto,command=lambda: youPick('paper'),relief="groove",padx=10)
    shandButton=Button(r_frame2,image=shandPhoto,command=lambda: youPick('scissor'),relief="groove",padx=10)
    rhandButton.pack(padx=3,side="left")
    phandButton.pack(padx=3,side="left")
    shandButton.pack(padx=3,side="left")

  def computerpick():
    choose=random.choice(['rock','paper','scissor'])
    return choose
  def youPick(yourChoice):
    global click
    click=True

    compPick=computerpick()
    if click==True:
      if yourChoice=='rock':
        rhandButton.configure(image= rockPhoto, state="disabled")
        if compPick=='rock':
          phandButton.configure(image= rockPhoto,state="disabled")
          shandButton.configure(image= tiePhoto,state="disabled")
          click=False
        elif compPick=='paper':
          phandButton.configure(image= paperPhoto,state="disabled")
          shandButton.configure(image= loosePhoto,state="disabled")
          click=False
        else:
          phandButton.configure(image= scissorPhoto,state="disabled")
          shandButton.configure(image= winnerPhoto,state="disabled")
          click==False

      if yourChoice=='paper':
        rhandButton.configure(image= paperPhoto,  state="disabled")
        if compPick=='rock':
          phandButton.configure(image= rockPhoto,state="disabled")
          shandButton.configure(image= winnerPhoto,state="disabled")
          click=False
        elif compPick=='paper':
          phandButton.configure(image= paperPhoto,state="disabled")
          shandButton.configure(image= tiePhoto,state="disabled")
          click=False
        else:
          phandButton.configure(image= scissorPhoto,state="disabled")
          shandButton.configure(image= loosePhoto,state="disabled")
          click==False

      if yourChoice=='scissor':
        rhandButton.configure(image=scissorPhoto,state="disabled")
        if compPick=='rock':
          phandButton.configure(image= rockPhoto,state="disabled")
          shandButton.configure(image= loosePhoto,state="disabled")
          click=False
        elif compPick=='paper':
          phandButton.configure(image= paperPhoto,state="disabled")
          shandButton.configure(image= winnerPhoto,state="disabled")
          click=False
        else:
          phandButton.configure(image= scissorPhoto,state="disabled")
          shandButton.configure(image= tiePhoto,state="disabled")
          click==False

  def yes():
    rhandButton.configure(image=rhandPhoto,state="normal")
    phandButton.configure(image=phandPhoto,state="normal")
    shandButton.configure(image=shandPhoto,state="normal")
  playgame()
  r_frame3 = Frame(root, bg="orange")
  r_frame3.pack(pady=20)
  Label(r_frame3,text="Do you want to play again: ",font=("arial",15), bg="orange").pack(side="left")
  yesbutton=Button(r_frame3, text="Yes",font=(10),width="15",height="3",bg="green",command=yes).pack(padx=20,side="left")
  nobutton=Button(r_frame3,text="No",font=(10),width="15",height="3",bg="red",command=root.quit).pack(side="left")

  root.mainloop()