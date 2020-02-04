from tkinter import *
from math import *


calculatrice = Tk()

label = Label(calculatrice,text="0")
label.place(x=10,y=10)

calculatrice.geometry("300x370+300+200")
nb1 = ""
test = ""
def ajout(nb):

	global nb1
	nb1+=nb
	label["text"] = nb1


def num0():
	ajout("0")

def num1():
	ajout("1")

def num2():
	ajout("2")

def num3():
	ajout("3")

def num4():
	ajout("4")

def num5():
	ajout("5")

def num6():
	ajout("6")

def num7():
	ajout("7")

def num8():
	ajout("8")
	
def num9():
	ajout("9")

def point():
	ajout(".")

def clear():
	global nb1, nb2
	nb1=""
	nb2=""
	label["text"] = ""
def plus():
	global nb1,op,nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 1
	label["text"] = "+"

def moins():
	global nb1,op,nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 2
	label["text"] = "-"

def mult():
	global nb1,op,nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 3
	label["text"] = "x"

def div():
	global nb1,op,nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 4
	label["text"] = "/"

def egal():
	global nb1
	nb1 = float(nb1)
	if(op == 1):
		result = round(nb2 + nb1, 10)
	elif(op == 2):
		result = round(nb2 - nb1, 10)
	elif(op == 3):
		result = round(nb2 * nb1, 10)
	elif(op == 4):
		result = round(nb2 / nb1, 10)
	nb1 = str(result)
	label["text"] = result
	result = 0



button = Button (calculatrice, text=" 0 ",command=num0, width=3, height=2, foreground="white", bg="grey").place(x=10, y=270)
button = Button (calculatrice, text=" 1 ",command=num1, width=3, height=2, foreground="white", bg="grey").place(x=10, y=120)
button = Button (calculatrice, text=" 2 ",command=num2, width=3, height=2, foreground="white", bg="grey").place(x=70, y=120)
button = Button (calculatrice, text=" 3 ",command=num3, width=3, height=2, foreground="white", bg="grey").place(x=130, y=120)
button = Button (calculatrice, text=" 4 ",command=num4, width=3, height=2, foreground="white", bg="grey").place(x=10, y=170)
button = Button (calculatrice, text=" 5 ",command=num5, width=3, height=2, foreground="white", bg="grey").place(x=70, y=170)
button = Button (calculatrice, text=" 6 ",command=num6, width=3, height=2, foreground="white", bg="grey").place(x=130, y=170)
button = Button (calculatrice, text=" 7 ",command=num7, width=3, height=2, foreground="white", bg="grey").place(x=10, y=220)
button = Button (calculatrice, text=" 8 ",command=num8, width=3, height=2, foreground="white", bg="grey").place(x=70, y=220)
button = Button (calculatrice, text=" 9 ",command=num9, width=3, height=2, foreground="white", bg="grey").place(x=130, y=220)
button_point = Button (calculatrice, text=" . ",command=point, width=3, height=2, foreground="white", bg="grey").place(x=70, y=270)

button_c = Button (calculatrice, text=" c ",command=clear, bg="red", width=3, height=2).place(x=190, y=70)
button_plus = Button (calculatrice, text=" + ",command=plus, width=3, height=2, foreground="white", bg="grey").place(x=190, y=270)
button_moins = Button (calculatrice, text=" - ",command=moins, width=3, height=2, foreground="white", bg="grey").place(x=190, y=220)
button_mult = Button (calculatrice, text=" x ",command=mult, width=3, height=2, foreground="white", bg="grey").place(x=190, y=170)
button_div = Button (calculatrice, text=" / ",command=div, width=3, height=2, foreground="white", bg="grey").place(x=190, y=120)
button_egal = Button (calculatrice, text=" = ",command=egal, width=3, height=2, foreground="white", bg="grey").place(x=130, y=270)
calculatrice.mainloop()