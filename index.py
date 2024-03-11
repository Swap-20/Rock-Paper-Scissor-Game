from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("ROCK SCISSOR PAPER GAME!")
root.config(background="black")

#picture
rock_img = ImageTk.PhotoImage(Image.open("user rock (2).png"))
paper_img = ImageTk.PhotoImage(Image.open("user paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("user scissor.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("comp rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("comp paper (2).png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Comp scissor (2).png"))

#insert picture
user_label = Label(root,image = rock_img, bg = "black")
comp_label = Label(root,image=rock_img_comp, bg = "black")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
playerscore = Label(root,text=0,font=100,bg="black",fg="white")
computerscore = Label(root,text=0,font=100,bg="black",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,bg="black",fg="white",text="USER")
comp_indicator = Label(root,font=50,bg="black",fg="white",text="COMPUTER")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root,font=50,bg="black",fg="white",text="You Loose")
msg.grid(row=3,column=2)

#update messages
def updatemessage(x):
    msg['text'] = x

#update user score
def updateuserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

#update computer score
def updatecompscore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

# checking winner
def checkWin(player,computer):
    if player == computer:
        updatemessage("Its a tie!!!")
    elif player == 'rock':
        if computer == 'paper':
            updatemessage('You loose')
            updatecompscore()
        else:
            updatemessage("You win")
            updateuserscore
    elif player == 'paper':
        if computer == 'scissor':
            updatemessage('You loose')
            updatecompscore()
        else:
            updatemessage('You win')
            updatecompscore()
    elif player == 'scissor':
        if computer == 'rock':
            updatemessage('You loose')
            updatecompscore()
        else:
            updatemessage('You win')
            updateuserscore()
    else:
        pass

#update choices
choices = ['rock','paper','scissor']
def updateChoices(x):

    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    #for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#ff3ead",fg="white",command= lambda:updateChoices("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#ff3ead",fg="white",command= lambda:updateChoices("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#ff3ead",fg="white",command= lambda:updateChoices("scissor")).grid(row=2,column=3)
root.mainloop()