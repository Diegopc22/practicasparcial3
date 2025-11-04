# Importamos los módulos necesarios de Tkinter
# Import the necessary Tkinter modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random 
from Validaciones import validar  # Importamos una clase personalizada para validaciones / Custom validation class

# Definición de la clase principal Ventana / Definition of the main class Window
class Ventana():
    def __init__(self):
        # Creamos una instancia de la clase validar / Create an instance of the validation class
        self.val = validar()
        # Creamos la ventana principal / Create the main window
        self.ven = Tk()
        self.ven.title('Programa 4')  # Título de la ventana / Window title

        # Dimensiones de la ventana / Window dimensions
        ancho = 500
        alto = 300
        ventana_alto = self.ven.winfo_screenmmwidth()  # Obtiene el ancho de pantalla en milímetros / Gets screen width in mm
        ventana_ancho = self.ven.winfo_screenmmwidth()  # (Posible error: debería ser height) / (Possible error: should be height)
        x = (ventana_alto // 2) - (ancho // 2)  # Calcula posición X centrada / Calculates centered X position
        y = (ventana_ancho // 2) - (alto // 2)  # Calcula posición Y centrada / Calculates centered Y position
        self.ven.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')  # Define tamaño y posición / Set size and position

        # Variables de control / Control variables
        self.con = 0           # Contador para generar claves / Counter to generate IDs
        self.bandera = False   # Bandera para modo edición / Flag for edit mode
        self.renglon = -1      # Índice de fila seleccionada / Selected row index
        self.index = 0         # Índice de clave actual / Current key index
    
    def Inicio(self):
        # Etiqueta y campo de entrada para el nombre / Label and entry for name
        Label(self.ven,text='Nombre').place(x=10,y=10)
        self.nombre = Entry(self.ven,fg="blue")
        self.nombre.place(x=10, y=30, width=100)

        #------------------------------------------------------
        # Etiqueta y campo de entrada para la edad / Label and entry for age
        Label(self.ven,text='Edad').place(x=120,y=10)
        self.edad = Entry(self.ven,fg="green")
        self.edad.place(x=120, y=30, width=100)

        #------------------------------------------------------
        # Etiqueta y campo de entrada para el correo / Label and entry for email
        Label(self.ven,text='Correo').place(x=230,y=10)
        self.correo = Entry(self.ven,fg="purple")
        self.correo.place(x=230, y=30, width=100)

        #------------------------------------------------------
        # Botones con sus respectivas funciones / Buttons with their functions
        Button(self.ven,text='Agregar',command=self.AgregarElemto).place(x=380,y=50,width=80)
        Button(self.ven,text='Eliminar',command=self.Eliminar).place(x=380,y=90,width=80)
        Button(self.ven,text='Seleccionar',command=self.Seleccionar).place(x=380,y=130,width=80)

        #------------------------------------------------------
        # Creación de la tabla / Create the data table
        columnas = ("Clave","Nombre","Corre","Edad")
        self.tabla = ttk.Treeview(self.ven,columns=columnas,show='headings')
        self.tabla.place(x=10,y=100,width=350,height=190)

        # Configuración de los encabezados / Set up column headers
        for col in columnas:
            self.tabla.heading(col,text=col)
            self.tabla.column(col,anchor='center',width=30)

        # Barras de desplazamiento / Scrollbars
        scrolly = ttk.Scrollbar(self.ven,orient='vertical',command=self.tabla.yview)
        scrollx = ttk.Scrollbar(self.ven,orient='horizontal',command=self.tabla.xview)
        scrolly.place(x=360,y=90,height=200)
        scrollx.place(x=10,y=280,width=350)

        # Iniciar la ventana principal / Start the main window loop
        self.ven.mainloop()

    def Seleccionar(self):
        # Obtiene el renglón seleccionado / Get selected row
        self.renglon = self.tabla.selection()
        if not self.renglon:
            # Muestra un mensaje si no se seleccionó nada / Show message if no selection
            messagebox.showerror('Error','Eligue una fila')
        else:
            # Obtiene los valores de la fila seleccionada / Get values from selected row
            valores = self.tabla.item(self.renglon,"values")
            print(valores)
            # Extrae el índice de la clave / Extract ID index
            self.index = valores[0]
            self.index = self.index[:len(self.index)-2]
            print(self.index)
            # Inserta los valores en los campos de texto / Insert values into entry fields
            self.nombre.insert(0,valores[1])
            self.edad.insert(0,valores[3])
            self.correo.insert(0,valores[2])
            self.bandera = True  # Activa el modo edición / Activate edit mode

    def AgregarElemto(self):
        # Verifica si hay campos vacíos / Check if any field is empty
        if len(self.nombre.get()) == 0 or len(self.edad.get()) == 0 or len(self.correo.get()) == 0:
            messagebox.showerror('Error','Faltan datos')
        else:
            # Obtiene los datos de las entradas / Get data from entries
            nombre = self.nombre.get()
            edad = self.edad.get()
            correo = self.correo.get()

            # Si no está en modo edición / If not in edit mode
            if self.bandera == False:
                self.con += 1  # Incrementa contador / Increase counter
                # Genera una clave única / Generate unique key
                clave = str(self.con)+str(random.randint(1,100))+self.nombre.get()[0:2].upper()
                # Inserta en la tabla / Insert into table
                self.tabla.insert("","end",values=(clave,nombre,correo,edad))
                # Limpia los campos / Clear entry fields
                self.nombre.delete(0,END)
                self.edad.delete(0,END)
                self.correo.delete(0,END)
            else:
                # Si está en modo edición / If in edit mode
                clave = self.index+self.nombre.get()[0:2].upper()
                print('Modo edicion activado')
                # Actualiza los valores de la fila seleccionada / Update selected row values
                self.tabla.item(self.renglon,values=(clave,nombre,correo,edad))
                # Limpia los campos / Clear fields
                self.nombre.delete(0,END)
                self.edad.delete(0,END)
                self.correo.delete(0,END)
                # Restablece los valores / Reset values
                self.bandera = False
                self.renglon = -1
                messagebox.showinfo('Correcto','Datos actualizados')
    
    def Eliminar(self):
        # Obtiene el renglón seleccionado / Get selected row
        self.renglon = self.tabla.selection()
        if not self.renglon:
            # Si no hay selección / If no selection
            messagebox.showerror('Error','Eligue una fila')
        else:
            # Muestra mensaje de eliminación y borra la fila / Show message and delete row
            messagebox.showinfo('Error','Fila eliminada')
            self.tabla.delete(self.renglon)


# Punto de entrada del programa / Program entry point
if __name__ == '__main__':
    app = Ventana()  # Crea una instancia de la clase Ventana / Create instance of Window class
    app.Inicio()     # Inicia la interfaz / Start the interface
