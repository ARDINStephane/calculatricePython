from tkinter import *
from math import *


calculatrice = Tk()

chaine = Label(calculatrice,text="")
resultat = Label(calculatrice, text="")
chaine.place(x=10,y=10)
resultat.place(x=10,y=30)
calculatrice.geometry("300x370+300+200")
nb1 = ""
nb2 = ""
res = False
rep = False
p = False
def ajout(nb):

        global nb1
        nb1+=nb
        chaine["text"] = nb1


def num0():
        ajout("0")
        testN()

def num1():
        testN()
        ajout("1")

def num2():
        testN()
        ajout("2")

def num3():
        testN()
        ajout("3")

def num4():
        testN()
        ajout("4")

def num5():
        testN()
        ajout("5")

def num6():
        testN()
        ajout("6")

def num7():
        testN()
        ajout("7")

def num8():
        testN()
        ajout("8")
        
def num9():
        testN()
        ajout("9")

def point():
        ajout(".")
        testN()
        testP()
def plus():
        global rep
        rep == True
        testA()
        ajout("+")

def moins():
        global rep
        rep == True       
        testA()
        ajout("-")

def mult():
        testA()
        ajout("*")
        testR()

def div():
        testA()
        ajout("/")
        testR()

def clear():
        global nb1, nb2, res, rep, p
        nb1=""
        nb2=""
        chaine["text"] = ""
        resultat["text"] = ""
        res=False
        rep=False
        p = False
def egal():
        global nb2, res, rep, p
        resultat.configure(text = " = " + str(eval(nb1)))
        nb2=str(eval(nb1))
        res = True
        rep = False
        p = False
def testA():
        global nb1,nb2, res, p
        res = False
        p = False
        if resultat["text"] != "":
              chaine["text"] = "" 
              nb1 = nb2 
              nb2 = ""
              chaine["text"] =  resultat["text"]
              resultat["text"] = ""
def testN():
        global res, rep
        rep = False
        if res == True:
                clear()
def testR():
        global rep, nb1
        if rep == True or nb1 == "*" or nb1 == "/":
                clear()
        rep = True

def testP():
        global p
        if p == True:
                clear()
        else:
                p=True

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
