from tkinter import *
from tkinter import messagebox
from Validaciones import Validar

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.ven.geometry('200x200')

    def validarCaja(self):
        valor = self.dato.get()
        if(self.val.ValidarNumeros(valor)):
            messagebox.showinfo('Correcto','Si es un numero')
        else:
            messagebox.showerror('Incorrecto','No es un numero')

    def Inicio(self):
        self.dato = Entry(self.ven)
        self.dato.place(x=50,y=10)
        Button(self.ven,text='Validar',command=self.validarCaja).place(x=100,y=50)
        self.ven.mainloop()


if __name__ == '__main__':
    app = Principal()
    app.Inicio()