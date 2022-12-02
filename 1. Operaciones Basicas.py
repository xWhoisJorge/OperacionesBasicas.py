#1 Operaciones Basicas de

from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def multiplicar():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()
    
def dividir():
    r.set( float(n1.get()) / float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
root.title("Operaciones Basicas")
root.config(bd=15)
root.geometry("400x300")
root.config(bg="#404258")
root.resizable(0,0)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

l1=Label(root, text="OPERACIONES BASICAS",fg="white", bg="#404258", font=("Arial",18,"bold"))
l1.pack()

ll1=Entry(root, justify="center", textvariable=n1)
ll1.pack()
ll1.place(x=125,y=60)

ll2=Entry(root, justify="center", textvariable=n2)
ll2.pack()
ll2.place(x=125, y=90)

l3=Entry(root, justify="center", textvariable=r)
l3.pack()
l3.place(x=125, y=200)

b1=Button(root, text="Sumar", command=sumar)
b1.pack()
b1.place(x=80,y=150)

b2=Button(root, text="Resta", command=resta)
b2.pack()
b2.place(x=135,y=150)

b3=Button(root, text="Multiplicar", command=multiplicar)
b3.pack()
b3.place(x=185,y=150)

b4=Button(root, text="Dividir", command=dividir)
b4.pack()
b4.place(x=265,y=150)

root.mainloop()