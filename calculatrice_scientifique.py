from math import *
from tkinter import *


calculatrice = Tk()

chaine = Label(calculatrice,text="", bd=5)
resultat = Label(calculatrice, text="")
chaine.place(x=10,y=10)
resultat.place(x=10,y=30)
calculatrice.geometry("315x360+350+200")

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
        testN()
        ajout("0")

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

def modulo():
        testA()
        ajout("%")
        testR()

def parentD():
        testN()
        ajout(")")

def parentG():
        testN()
        ajout("(")

def coss():
        testN()    
        ajout("cos(")

def sins():
        testN()
        ajout("sin(")

def tann():
        testN()
        ajout("tan(")

def EXP():
        testN()
        ajout("E")

def C():
        global nb1
        testN()
        nb1 = nb1[:-1]
        chaine["text"] = nb1
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
        res = True
        rep = False
        p = False        
        try:
            resultat.configure(text = " = " + str(eval(nb1)))
        except SyntaxError: 
            nb2 = "Error"
            resultat["text"] = "Error"  
        except TypeError:  
            nb2 = "Error"
            resultat["text"] = "Error"      
        except NameError:  
            nb2 = "Error"
            resultat["text"] = "Error"                        
        nb2=str(eval(nb1))       


def testA():
        global nb1,nb2, res, p
        res = False
        p = False
        if resultat["text"] != "" and nb2 != "Error":
              chaine["text"] = "" 
              nb1 = nb2 
              nb2 = ""
              chaine["text"] =  resultat["text"]
              resultat["text"] = ""
        elif nb2 == "Error":
            clear()

def testN():
        global res, rep, nb2
        rep = False
        if res == True or nb2 == "Error":
                clear()

def testR():
        global rep, nb1
        if rep == True or nb1 == "*" or nb1 == "/" or nb1 == "%" or nb1 == "tan":
                clear()
        rep = True

def testP():
        global p
        if p == True:
                clear()
        else:
                p=True

button = Button (calculatrice, text=" 0 ",command=num0, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=10, y=270)
button = Button (calculatrice, text=" 1 ",command=num1, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=10, y=120)
button = Button (calculatrice, text=" 2 ",command=num2, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=70, y=120)
button = Button (calculatrice, text=" 3 ",command=num3, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=130, y=120)
button = Button (calculatrice, text=" 4 ",command=num4, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=10, y=170)
button = Button (calculatrice, text=" 5 ",command=num5, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=70, y=170)
button = Button (calculatrice, text=" 6 ",command=num6, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=130, y=170)
button = Button (calculatrice, text=" 7 ",command=num7, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=10, y=220)
button = Button (calculatrice, text=" 8 ",command=num8, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=70, y=220)
button = Button (calculatrice, text=" 9 ",command=num9, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=130, y=220)
button_point = Button (calculatrice, text=" . ",command=point, width=3, height=2, foreground="white", bg="#BDBDBD").place(x=70, y=270)

button_c = Button (calculatrice, text=" DEL ",command=C, bg="red", width=3, height=2).place(x=190, y=70)
button_plus = Button (calculatrice, text=" + ",command=plus, width=3, height=2, foreground="white", bg="grey").place(x=190, y=270)
button_moins = Button (calculatrice, text=" - ",command=moins, width=3, height=2, foreground="white", bg="grey").place(x=190, y=220)
button_mult = Button (calculatrice, text=" x ",command=mult, width=3, height=2, foreground="white", bg="grey").place(x=190, y=170)
button_div = Button (calculatrice, text=" / ",command=div, width=3, height=2, foreground="white", bg="grey").place(x=190, y=120)
button_egal = Button (calculatrice, text=" = ",command=egal, width=3, height=2, foreground="white", bg="#0040FF").place(x=130, y=270)

button_plus = Button (calculatrice, text=" % ",command=modulo, width=3, height=2, foreground="white", bg="grey").place(x=130, y=70)
button_plus = Button (calculatrice, text=" ( ",command=parentG, width=3, height=2, foreground="white", bg="grey").place(x=10, y=70)
button_plus = Button (calculatrice, text=" ) ",command=parentD, width=3, height=2, foreground="white", bg="grey").place(x=70, y=70)
button_plus = Button (calculatrice, text=" EXP ",command=EXP, width=3, height=2, foreground="white", bg="#2E9AFE").place(x=250, y=270)

button_plus = Button (calculatrice, text=" AC ",command=clear, width=3, height=2, bg="#B40404").place(x=250, y=70)
button_plus = Button (calculatrice, text=" sin ",command=sins, width=3, height=2, foreground="white", bg="#2E9AFE").place(x=250, y=120)
button_plus = Button (calculatrice, text=" cos ",command=coss, width=3, height=2, foreground="white", bg="#2E9AFE").place(x=250, y=170)
button_plus = Button (calculatrice, text=" tan ",command=tann, width=3, height=2, foreground="white", bg="#2E9AFE").place(x=250, y=220)

calculatrice.mainloop()
