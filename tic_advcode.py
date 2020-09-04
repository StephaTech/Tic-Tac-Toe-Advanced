# code copyright from DJ Oamen from his youtube channel
import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='Cadet Blue')

Tops = Frame(root,bg = 'Cadet Blue',pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0,column=0)

lblTitle = Label(Tops, font=('arial',50,'bold'), text="Advanced Tic Tac Toe Game", bd=21, bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=1, column=0)#defining font, size of title

MainFrame = Frame(root, bg ='Powder Blue', bd=10, width = 1350, height=600, relief =RIDGE)
MainFrame.grid(row=1, column=0)#bd -->gave border white

LeftFrame = Frame(MainFrame, bd=10,width =750,heigh=500,pady=2,padx=10,bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=750, height= 500, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, padx=10,pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame , bd=10, width=560, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

button = StringVar()

lblPlayerX =Label(RightFrame1, font=('arial', 40, 'bold'), text="Player X :",padx=2, pady=2, bg="Cadet Blue")
lblPlayerX.grid(row=0, column=0, sticky=W)

lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player O :",padx=2, pady=2, bg="Cadet Blue")
lblPlayerO.grid(row=1, column=0, sticky=W)

button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button2.grid(row=1,column=1, sticky=S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7= Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button7.grid(row=3, column= 0, sticky=S+N+E+W)

button8= Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button8.grid(row=3, column= 1, sticky=S+N+E+W)

button9= Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro')
button9.grid(row=3, column= 2, sticky=S+N+E+W)



root.mainloop()#visualize the frame
