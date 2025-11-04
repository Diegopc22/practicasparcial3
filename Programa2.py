"""Hacer un programa que lea nombre, apellido parterno y apellido materno en tre cajas separadas ademas ler dia, mes y año de nacimiento en 3
cajas separadas. al precionar un boton se agregara  un lisbox el rfc de la persona, ademas contendra dos botones para eliminar elemntos del lixbox 
mediante pilas y colas"""
# Description: This program reads name, paternal and maternal surnames in separate input boxes, 
# as well as day, month, and year of birth. When pressing a button, the RFC of the person is added 
# to a listbox. It also has two buttons to remove elements from the listbox using stack or queue logic.

from tkinter import *                      # Importa todas las clases y funciones de tkinter / Imports all classes and functions from tkinter
from tkinter import messagebox              # Importa messagebox para mostrar mensajes emergentes / Imports messagebox for pop-up alerts
from Validaciones2 import validar           # Importa la clase 'validar' del archivo Validaciones2 / Imports the 'validar' class from Validaciones2

class Ventana():                            # Define la clase principal / Defines the main class
    def __init__(self):                     # Constructor de la clase / Class constructor
        self.ven = Tk()                     # Crea la ventana principal / Creates the main window
        self.ven.title('Programa 2')        # Asigna título a la ventana / Sets window title
        self.ven.geometry('650x300')        # Define el tamaño de la ventana / Sets window size
        self.val = validar()                # Crea una instancia del validador / Creates an instance of the validator
        self.lista = []                     # Lista para almacenar RFCs / List to store RFCs

    def Inicio(self):                       # Método que inicializa los elementos de la interfaz / Method that initializes GUI elements
        Label(self.ven,text='Nombre').place(x=10,y=10)           # Etiqueta para el nombre / Label for name
        self.nombre = Entry(self.ven)                            # Caja de texto para el nombre / Entry for name
        self.nombre.place(x=10,y=40)

        Label(self.ven,text='Apellido paterno').place(x=165,y=10) # Etiqueta para el apellido paterno / Label for paternal surname
        self.paterno = Entry(self.ven)                            # Caja de texto para el apellido paterno / Entry for paternal surname
        self.paterno.place(x=165,y=40)

        Label(self.ven,text='Apellido materno').place(x=320,y=10) # Etiqueta para el apellido materno / Label for maternal surname
        self.materno = Entry(self.ven)                            # Caja de texto para el apellido materno / Entry for maternal surname
        self.materno.place(x=320,y=40)

        # --------------------------------------------------------
        Label(self.ven,text='FECHA DE NACIMIENTO').place(x=175,y=80)  # Título de la sección / Section title: Date of birth
        Label(self.ven,text='Dia').place(x=10,y=120)                  # Etiqueta del día / Label for day
        self.dia = Entry(self.ven)                                   # Caja de texto del día / Entry for day
        self.dia.place(x=10,y=150)

        Label(self.ven,text='Mes').place(x=165,y=120)                 # Etiqueta del mes / Label for month
        self.mes = Entry(self.ven)                                   # Caja de texto del mes / Entry for month
        self.mes.place(x=165,y=150)

        Label(self.ven,text='Año').place(x=320,y=120)                 # Etiqueta del año / Label for year
        self.año = Entry(self.ven)                                   # Caja de texto del año / Entry for year
        self.año.place(x=320,y=150)

        # ---------------------------------------------------------
        self.modo = StringVar(value='Pilas')                         # Variable para el modo de eliminación / Variable for delete mode (stack/queue)
        Button(self.ven,text='Calcular RFC',command=self.Calcular).place(x=10,y=180)  # Botón para calcular RFC / Button to calculate RFC
        Button(self.ven,text='Eliminar',command=self.Eliminar).place(x=320,y=180)     # Botón para eliminar RFC / Button to delete RFC
        Radiobutton(self.ven,text='Pilas',variable=self.modo, value='Pilas').place(x=165, y=180)  # Radio botón para modo pila / Radio button for stack
        Radiobutton(self.ven,text='Colas',variable=self.modo, value='Colas').place(x=235, y=180)  # Radio botón para modo cola / Radio button for queue
        self.listview = Listbox(self.ven, height=10, width=15, bg='grey', activestyle="dotbox", fg="Black")  # Listbox para mostrar RFCs / Listbox to show RFCs
        self.listview.place(x=480, y=10)
        self.ven.mainloop()                                          # Inicia el bucle principal de la interfaz / Starts the GUI main loop

    def Calcular(self):                                              # Método para calcular el RFC / Method to calculate RFC
        a = False; b = False; c = False; d = False; e = False; f = False  # Flags para validaciones / Flags for validation
        nombre = self.nombre.get()                                   # Obtiene el nombre / Gets name
        paterno = self.paterno.get()                                 # Obtiene apellido paterno / Gets paternal surname
        materno = self.materno.get()                                 # Obtiene apellido materno / Gets maternal surname
        dia = self.dia.get()                                         # Obtiene el día / Gets day
        mes = self.mes.get()                                         # Obtiene el mes / Gets month
        anio = self.año.get()                                        # Obtiene el año / Gets year

        if nombre != "" and paterno != "" and materno != "" and dia != "" and mes != "" and anio != "":  
            # Verifica que no haya campos vacíos / Checks that no fields are empty

            if self.val.ValidarLetra(nombre): a = True               # Valida nombre / Validates name
            else:
                messagebox.showerror('Error','Nombre incorrecto')    # Error si no es válido / Error if invalid
                self.nombre.delete(0,END)

            if self.val.ValidarLetra(paterno): b = True              # Valida apellido paterno / Validates paternal surname
            else:
                messagebox.showerror('Error','Apellido paterno incorrecto')
                self.paterno.delete(0,END)

            if self.val.ValidarLetra(materno): c = True              # Valida apellido materno / Validates maternal surname
            else:
                messagebox.showerror('Error','Apellido materno incorrecto')
                self.materno.delete(0,END)

            if self.val.ValidarNumeros(dia):                         # Valida que día sea numérico / Validates day is numeric
                if int(dia) < 1 or int(dia) > 31:                    # Comprueba rango válido / Checks valid range
                    messagebox.showerror('Error','Dia inválido')
                    self.dia.delete(0,END)
                else:
                    d = True
            else:
                messagebox.showerror('Error','Dia inválido')
                self.mes.delete(0,END)

            if self.val.ValidarNumeros(mes):                         # Valida mes / Validates month
                if int(mes) < 1 or int(mes) > 12:                    # Comprueba rango válido / Checks valid range
                    messagebox.showerror('Error','Mes inválido')
                    self.mes.delete(0,END)
                else:
                    e = True
            else:
                messagebox.showerror('Error','Mes inválido')
                self.mes.delete(0,END)

            if self.val.ValidarNumeros(anio):                        # Valida año / Validates year
                if len(anio) > 4:                                    # Máximo 4 dígitos / Max 4 digits
                    messagebox.showerror('Error','Año inválido')
                    self.año.delete(0,END)
                else:
                    f = True
            else:
                messagebox.showerror('Error','Año inválido')
                self.año.delete(0,END)

            # Si todo está correcto, calcula RFC / If all checks pass, calculates RFC
            if a == True and b == True and c == True and d == True and e == True and f == True:
                # Formato RFC: 2 primeras del paterno + 1 del materno + 1 del nombre + año + mes + día / RFC format
                self.rfc = paterno[0:2].upper()+materno[0].upper()+nombre[0].upper()+anio[2:]+mes.zfill(2)+dia.zfill(2)
                self.listview.insert(self.listview.size()+1,self.rfc) # Agrega RFC al Listbox / Adds RFC to Listbox

                # Limpia todas las cajas / Clears all input boxes
                self.nombre.delete(0,END)
                self.paterno.delete(0,END)
                self.materno.delete(0,END)
                self.dia.delete(0,END)
                self.mes.delete(0,END)
                self.año.delete(0,END)
        else:
            # Error si alguna caja está vacía / Error if any field is empty
            messagebox.showerror('Error', "Cajas de texto vacías")
            self.nombre.delete(0,END)
            self.paterno.delete(0,END)
            self.materno.delete(0,END)
            self.dia.delete(0,END)
            self.mes.delete(0,END)
            self.año.delete(0,END)

    def Eliminar(self):                                              # Método para eliminar elementos del Listbox / Method to delete list elements
        if self.listview.size() <= 0:                                # Si está vacío / If empty
            messagebox.showerror('Error','La lista está vacía')      # Muestra error / Shows error
            return
        if self.modo.get() == 'Pilas':                               # Si modo es "Pilas" / If mode is Stack
            self.listview.delete(self.listview.size()-1)             # Elimina último elemento / Removes last item
        else:                                                        # Si modo es "Colas" / If mode is Queue
            self.listview.delete(0)                                  # Elimina primer elemento / Removes first item

if __name__ == '__main__':                                           # Punto de entrada / Program entry point
    app = Ventana()                                                  # Crea instancia de la clase Ventana / Creates instance of Ventana class
    app.Inicio()                                                     # Llama al método para iniciar la interfaz / Calls GUI start method
