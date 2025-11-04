from tkinter import *                          # Importa todas las clases y funciones de Tkinter / Imports all Tkinter classes and functions
from tkinter import messagebox                 # Importa la función de mensajes emergentes / Imports the messagebox function
from Validaciones import validar               # Importa la clase 'validar' del archivo Validaciones.py / Imports the 'validar' class from Validaciones.py

class Ventana():
    def __init__(self):
        self.val = validar()                   # Crea un objeto de la clase validar / Creates an object from the validar class
        self.ven = Tk()                        # Crea la ventana principal de la aplicación / Creates the main application window
        self.ven.title('Programa 3')           # Asigna el título de la ventana / Sets the window title
        ancho = 350                            # Define el ancho de la ventana / Defines window width
        alto = 250                             # Define el alto de la ventana / Defines window height
        ventana_alto = self.ven.winfo_screenmmwidth()  # Obtiene el alto de la pantalla en milímetros / Gets screen height in millimeters
        ventana_ancho = self.ven.winfo_screenmmwidth() # Obtiene el ancho de la pantalla en milímetros / Gets screen width in millimeters
        x = (ventana_alto // 2) - (ancho // 2) # Calcula la posición horizontal centrada / Calculates centered horizontal position
        y = (ventana_ancho // 2) - (alto // 2) # Calcula la posición vertical centrada / Calculates centered vertical position
        self.ven.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')  # Define el tamaño y posición de la ventana / Sets window size and position
    
    # ---------------- MÉTODOS PARA PLACEHOLDERS ---------------- #
    def quitar_placeholder1(self, event):
        # Si el texto actual es igual al placeholder, se borra el texto y se cambia el color / 
        # If the current text equals the placeholder, delete it and change text color
        if self.nombre.get() == self.placeholder1:
            self.nombre.delete(0, END)
            self.nombre.config(fg="black")

    def poner_placeholder1(self, event):
        # Si el campo está vacío, se vuelve a poner el placeholder / 
        # If the field is empty, reinsert the placeholder
        if self.nombre.get() == "":
            self.nombre.insert(0, self.placeholder1)
            self.nombre.config(fg="gray")

    def quitar_placeholder2(self, event):
        # Borra el texto del segundo campo si es igual al placeholder / 
        # Clears text if it matches placeholder (for second entry)
        if self.telefono.get() == self.placeholder2:
            self.telefono.delete(0, END)
            self.telefono.config(fg="black")

    def poner_placeholder2(self, event):
        # Restaura el placeholder si el campo está vacío / 
        # Restores placeholder if field is empty
        if self.telefono.get() == "":
            self.telefono.insert(0, self.placeholder2)
            self.telefono.config(fg="gray")

    def quitar_placeholder3(self, event):
        # Borra el texto del tercer campo si es igual al placeholder / 
        # Clears text if it matches placeholder (for third entry)
        if self.domicilio.get() == self.placeholder3:
            self.domicilio.delete(0, END)
            self.domicilio.config(fg="black")

    def poner_placeholder3(self, event):
        # Restaura el placeholder si el campo está vacío / 
        # Restores placeholder if field is empty
        if self.domicilio.get() == "":
            self.domicilio.insert(0, self.placeholder3)
            self.domicilio.config(fg="gray")

    # ---------------- CONFIGURACIÓN DE LA INTERFAZ ---------------- #
    def Inicio(self):
        # Campo de texto para el nombre / Name input field
        self.placeholder1 = 'Nombre'
        self.nombre = Entry(self.ven, fg="gray")               # Crea una caja de texto con texto gris / Creates an entry with gray text
        self.nombre.insert(0, self.placeholder1)               # Inserta el texto "Nombre" como placeholder / Inserts "Nombre" as placeholder
        self.nombre.bind("<FocusIn>", self.quitar_placeholder1)# Quita el placeholder al enfocar / Removes placeholder on focus
        self.nombre.bind("<FocusOut>", self.poner_placeholder1)# Restaura placeholder al perder foco / Restores placeholder on focus out
        self.nombre.bind("<Return>", self.ValidarCaja)         # Valida al presionar Enter / Validates on pressing Enter
        self.nombre.place(x=10, y=10, width=100)               # Coloca el campo en pantalla / Places the field on screen
        
        # Campo de texto para el teléfono / Phone input field
        self.placeholder2 = "Telefono"
        self.telefono = Entry(self.ven, fg="gray")             # Crea la caja de texto gris / Creates gray text entry
        self.telefono.insert(0, self.placeholder2)             # Inserta el texto "Telefono" como placeholder / Inserts "Telefono" placeholder
        self.telefono.bind("<FocusIn>", self.quitar_placeholder2)
        self.telefono.bind("<FocusOut>", self.poner_placeholder2)
        self.telefono.bind("<Return>", self.ValidarCaja)
        self.telefono.place(x=120, y=10, width=100)

        # Campo de texto para domicilio / Address input field
        self.domicilio = Entry(self.ven, fg="gray")
        self.placeholder3 = "Dimicilio"                       # (Error tipográfico: debería ser Domicilio) / Typo: should be “Domicilio”
        self.domicilio.insert(0, self.placeholder3)
        self.domicilio.bind("<FocusIn>", self.quitar_placeholder3)
        self.domicilio.bind("<FocusOut>", self.poner_placeholder3)
        self.domicilio.bind("<Return>", self.ValidarCaja)
        self.domicilio.place(x=230, y=10, width=100)

        # Etiqueta y botones de selección de sexo / Label and radio buttons for gender
        Label(self.ven, text='Sexo').place(x=10, y=30)         # Muestra el texto "Sexo" / Displays the word “Sexo”
        self.modo = StringVar(value='F')                       # Variable para guardar el valor seleccionado / Variable to store selected value
        Radiobutton(self.ven, text='F', variable=self.modo, value='F').place(x=10, y=50)  # Opción femenina / Female option
        Radiobutton(self.ven, text='M', variable=self.modo, value='M').place(x=10, y=70)  # Opción masculina / Male option
        
        # Lista para mostrar los datos agregados / Listbox to display added data
        self.lista = Listbox(self.ven, height=8, width=30, bg='grey', activestyle="dotbox", fg="Black")
        self.lista.place(x=10, y=100)

        # Botón para agregar a la lista / Button to add data to the list
        Button(self.ven, text='Agregar', command=self.ValidarCaja, width=10).place(x=210, y=100, width=100, height=50)

        # Mantiene la ventana abierta / Keeps window running
        self.ven.mainloop()

    # ---------------- FUNCIÓN PARA VALIDAR Y AGREGAR DATOS ---------------- #
    def ValidarCaja(self, event=0):
        a = False   # Variable para validar nombre / Flag to validate name
        b = False   # Variable para validar teléfono / Flag to validate phone number

        # Verifica que los campos no estén vacíos o con placeholders / Checks that fields are not empty or placeholders
        if (self.nombre.get() == self.placeholder1 or 
            self.telefono.get() == self.placeholder2 or 
            self.domicilio.get() == self.placeholder3 or 
            self.domicilio.get() == ""):
            messagebox.showerror('Error','Faltan datos')       # Muestra error si faltan datos / Shows error if fields are missing
        else:
            # Obtiene los valores de los campos / Gets input values
            nombre = self.nombre.get()
            telefono = self.telefono.get()
            domicilio = self.domicilio.get()

            # Determina el sexo según el radiobutton / Determines gender based on radio button
            if self.modo.get() == 'F':
                sexo = 'Femenino'
            else:
                sexo = 'Masculino'
            
            # Valida que el nombre contenga solo letras / Checks that name has only letters
            if self.val.ValidarLetra(nombre):
                a = True
            else:
                self.nombre.delete(0, END)
                messagebox.showerror('Error','Nombre incorrecto') # Error si contiene caracteres inválidos / Error if invalid characters

            # Valida que el teléfono contenga solo números / Checks that phone number has only digits
            if self.val.ValidarNumeros(telefono):
                if len(telefono) == 10:                         # Requiere 10 dígitos / Requires 10 digits
                    b = True
                else:
                    self.telefono.delete(0, END)
                    messagebox.showerror('Error','Telefono incorrecto')
            else:
                self.telefono.delete(0, END)
                messagebox.showerror('Error','Telefono incorrecto')
            
            # Si ambas validaciones son correctas / If both validations pass
            if a == True and b == True:
                clabe = nombre[0]+telefono[0]+domicilio[0]      # Crea una clave con las iniciales / Creates key with initials
                persona = clabe+"-"+nombre+"-"+telefono+"-"+domicilio+"-"+sexo  # Une toda la información en una cadena / Combines info into a string
                self.lista.insert(self.lista.size()+1, persona)  # Agrega la persona a la lista / Inserts person into listbox

# Punto de entrada del programa / Program entry point
if __name__ == '__main__':
    app = Ventana()         # Crea un objeto de la clase Ventana / Creates an instance of Ventana
    app.Inicio()            # Inicia la interfaz gráfica / Starts the GUI