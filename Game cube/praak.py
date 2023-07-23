import random
import tkinter
from Root import root
from tkinter.ttk import *
from PIL import ImageTk, Image
def mygame():
    root.title("Fight Game - Menu")
    root.configure(background="red", cursor="arrow")
    root.geometry("978x550")
    logo=tkinter.Canvas(root,bg="black",height=232,width=595)
    img = ImageTk.PhotoImage(Image.open("Street Fighter.png"))
    logo.create_image(300,30, anchor = "n",image = img)
    logo.pack()   
    ig=Image.open("Fight1.jpg")
    ig2=ig.resize((225,100),Image.ANTIALIAS)
    ig2=ImageTk.PhotoImage(ig2)
    menustrt=tkinter.Button(root, text="Start",image = ig2, command=gameplay) 
    fightl=tkinter.Label(root, text="PRESS FIGHT TO START GAME",font=("Cooper black", 14), bg="red", fg="white")
    menuxit=tkinter.Button(root, text="QUIT", command=exit)
    menuxit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    menustrt.pack(side=tkinter.TOP)
    fightl.pack()
    root.mainloop()
def gameplay():
    root.destroy()
    window=tkinter.Tk()
    window.title("Fight Game - Playing")
    window.configure(background="red", cursor="arrow")
    window.geometry("600x550")

    global basehp
    global health
    global tdmgp
    global tdmg
    tdmg=0
    tdmgp=0
    pmodifier=1.5
    kmodifier=0.5
    gmodifier=0.25
    health=200
    basehp=200
        
    global ehealth
    ehealth=health
    global ebasehp
    ebasehp=basehp

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            ehealthl.configure(text="Health: 0"+"/"+str(ebasehp))
            #print("Player has won")
            global pwin
            pwin=1
            winner.configure(text="Player has won")

    def ewin():
        global health
        if health<=0:
            healthl.configure(text="Health: 0"+"/"+str(basehp))
            #print("Enemy has won")
            global pwin
            pwin=1
            winner.configure(text="Enemy has won")
    def eattack():
        global pwin
        if pwin!=1:
         global health
         global ehealth
         dmgdealt=int(round(random.randint(21,30)))
         health-=dmgdealt
         #print("Player health is now: "+str(health))
         healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
         enemymove.configure(text="Enemy used: Magical spells and attacks: "+(str(dmgdealt)))
         pwin()
         ewin()

    def attackp():  
        global pwin
        if pwin!=1:
            global ehealth
            global dmgdealtp
            dmgdealtp=int(round(random.randint(21,30)))
            ehealth-=dmgdealtp
            ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
            playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            ewin()
            eattack()
    def restart():
        window.destroy()
        mygame()
	
   
    player=tkinter.Label(window, text="Player", font=("Cooper black", 24, "italic"))
    healthl=tkinter.Label(window, text=("Health: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
    enemy=tkinter.Label(window, text="Enemy", font=("Cooper black", 24, "italic"))
    ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
    igm=Image.open("Fight2.png")
    igm2=igm.resize((225,100),Image.ANTIALIAS)
    igm2=ImageTk.PhotoImage(igm2)   
    pattack=tkinter.Button(window, text="Attack",image=igm2, command=attackp)
    restart=tkinter.Button(window, text="Restart", command=restart)
    texit=tkinter.Button(window, text="Exit", command=exit)
    enemymove=tkinter.Label(window,text="", font=("Courier", 18,"italic"), bg="red",fg="white")
    playerddealt=tkinter.Label(window,text="", font=("Courier", 18,"italic"), bg="red", fg="white")
    winner=tkinter.Label(window, text="", font=("Cooper black", 32, "italic"), bg="red", fg="white")
    pattack.pack()
    texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    player.pack(pady=10, padx=20, fill=tkinter.X)
    healthl.pack()
    pattack.pack(pady=5)
    playerddealt.pack()
    enemy.pack(pady=10, padx=20, fill=tkinter.X)
    ehealthl.pack()
    enemymove.pack()
    restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    winner.pack(side=tkinter.BOTTOM)
    window.mainloop()


