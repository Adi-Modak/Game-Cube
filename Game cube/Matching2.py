from Root import *
from tkinter import *
from tkinter import messagebox
import random


def play():
    root.title(" Tile Match")
    my_label = Label(root, text="Matching Game",font=(15),bg="maroon", width=44)
    my_label.pack(pady=30)

    my_frame = Frame(root)
    my_frame.pack(pady=20)

    global i,answer_list,answer_dict,winner,pairs 
    pairs=[]
    pairs = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(pairs)

    i=0
    answer_list = []
    answer_dict = {}
    winner=0

    def yes():
        global winner, pairs
        winner = 0
        pairs = [1,1,2,2,3,3,4,4,5,5,6,6]
        random.shuffle(pairs)
        my_label1.configure(text="", bg="orange")
        button_list = [button0, button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11]
        for j in button_list:
            j.configure(text=" ",bg="SystemButtonFace", state="normal")
    def click(my_button,number):
        global i,answer_list,answer_dict,winner,pairs
        if my_button["text"] == ' ' and i < 2:
            my_button["text"] = pairs[number]
            answer_list.append(number)
            answer_dict[my_button] = pairs[number]
            i += 1

            if len(answer_list) == 2:
                if pairs[answer_list[0]] == pairs[answer_list[1]]:
                    my_label1.configure(text="Match!!", bg="yellow") 
                    winner+=1 
                    for key in answer_dict:
                        key["state"] = "disabled"
                    i = 0
                    answer_list = []
                    answer_dict = {}
                    if winner==6:
                        my_label1.configure(text="Congratulation! You Won!!", bg="green")
                        button_list = [button0, button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11]
                        for j in button_list:
                            j.configure(bg="cyan")
                else:
                    my_label1.configure(text="OHHH!!! NOOOOO...", bg="red")
                    i = 0
                    answer_list = []
                    messagebox.showinfo("Incorrect")
                    for key in answer_dict:
                        key["text"] = " "
                    answer_dict = {}

    button0 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button0,0), relief="groove")
    button0.grid(row=1,column=0)

    button1 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button1,1), relief="groove")
    button1.grid(row=1,column=1)

    button2 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button2,2), relief="groove")
    button2.grid(row=1,column=2)

    button3 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button3,3), relief="groove")
    button3.grid(row=1,column=3)

    button4 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button4,4), relief="groove")
    button4.grid(row=2,column=0)

    button5 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button5,5), relief="groove")
    button5.grid(row=2,column=1)

    button6 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button6,6), relief="groove")
    button6.grid(row=2,column=2)

    button7 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button7,7), relief="groove")
    button7.grid(row=2,column=3)

    button8 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button8,8), relief="groove")
    button8.grid(row=3,column=0)

    button9 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button9,9), relief="groove")
    button9.grid(row=3,column=1)

    button10 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button10,10), relief="groove")
    button10.grid(row=3,column=2)

    button11 = Button(my_frame, text=" ", width=10, height=5, font=(10), command=lambda:click(button11,11), relief="groove")
    button11.grid(row=3,column=3)

    my_label1 = Label(root,text="", bg="orange")
    my_label1.pack()

    my_frame1 = Frame(root, bg="orange")
    my_frame1.pack(pady=20)

    yes_button = Button(my_frame1, text="New Game", bg="green", command=yes).pack(side=LEFT,padx=10, ipadx=20, ipady=5)
    no_button = Button(my_frame1, text= "Quit",bg="red",command=root.quit).pack(side=LEFT,padx=10, ipadx=40, ipady=5)

    root.mainloop()