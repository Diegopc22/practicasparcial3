from tkinter import *               # Importa todas las funciones y clases del módulo tkinter (para crear interfaces gráficas)
from tkinter import messagebox      # Importa el módulo messagebox para mostrar mensajes emergentes (alertas o errores)
from Validaciones import validar    # Importa la clase 'validar' del archivo Validaciones.py
import numpy as np                  # Importa la librería numpy (para manejar arreglos numéricos)

# ------------------------------------------------------------
# Clase Principal que controla la ventana y las funciones del programa
# Main class that manages the window and the program functions
# ------------------------------------------------------------
class Principal():
    def __init__(self):  # Constructor de la clase / Class constructor
        self.val = validar()                         # Crea una instancia de la clase validar / Creates an instance of the 'validar' class
        self.ven = Tk()                              # Crea la ventana principal / Creates the main window
        self.ven.title('Programa 1')                 # Asigna el título de la ventana / Sets window title
        
        # Tamaño y posición de la ventana / Window size and position
        ancho = 400                                  # Ancho de la ventana / Window width
        alto = 275                                   # Alto de la ventana / Window height
        ventana_alto = self.ven.winfo_screenmmwidth()  # Obtiene el ancho de la pantalla (en mm) / Gets screen width (in mm)
        ventana_ancho = self.ven.winfo_screenmmwidth() # (Probablemente un error, debería ser 'winfo_screenheight') / Likely a typo
        x = (ventana_alto // 2) - (ancho // 2)       # Calcula posición X centrada / Calculates centered X position
        y = (ventana_ancho // 2) - (alto // 2)       # Calcula posición Y centrada / Calculates centered Y position
        self.ven.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')  # Define tamaño y posición / Sets window size and position
        self.lis = []                                # Lista vacía para almacenar valores / Empty list to store values

    # ------------------------------------------------------------
    # Método para validar el dato ingresado / Method to validate input
    # ------------------------------------------------------------
    def validarcaja(self):
        valor = self.dato.get()                      # Obtiene el texto del campo de entrada / Gets text from Entry
        if (self.val.ValidarNumeros(valor)):         # Verifica si son números / Checks if input is numeric
            if (self.val.ValidarEntradas(valor)):    # Verifica que tenga máximo dos dígitos / Checks if it has at most two digits
                self.listview.insert(self.listview.size()+1, valor)  # Agrega valor al Listbox / Adds value to Listbox
                self.dato.delete(0, END)             # Limpia la caja de texto / Clears the Entry box
            else:
                messagebox.showerror('Error', 'Solo se permiten dos dígitos')  # Error si tiene más de dos dígitos / Error for too many digits
                self.dato.delete(0, END)
        else:
            messagebox.showerror('Error', 'No son números')  # Error si no es numérico / Error if not numeric
            self.dato.delete(0, END)
        # Actualiza el texto del label con la cantidad de elementos / Updates label with number of elements
        self.label.config(text=f'Numero de elementos: {str(self.listview.size())}')

    # ------------------------------------------------------------
    # Método para eliminar datos de la lista / Method to remove data from list
    # ------------------------------------------------------------
    def EliminarDato(self):
        if self.listview.size() <= 0:                # Si la lista está vacía / If list is empty
            messagebox.showerror('Error', 'La lista está vacía')  # Muestra error / Shows error message
            return
        if self.modo.get() == 'Pilas':               # Si el modo es "Pilas" (LIFO) / If mode is "Stack"
            self.listview.delete(self.listview.size()-1)  # Elimina el último elemento / Removes last element
        else:                                        # Si el modo es "Colas" (FIFO) / If mode is "Queue"
            self.listview.delete(0)                  # Elimina el primer elemento / Removes first element
        # Actualiza el contador / Updates counter
        self.label.config(text=f'Numero de elementos:  {str(self.listview.size())}')

    # ------------------------------------------------------------
    # Método para ordenar los datos / Method to sort the data
    # ------------------------------------------------------------
    def Ordenar(self):
        if self.listview.size() <= 0:                # Verifica si la lista está vacía / Checks if list is empty
            messagebox.showerror('Error','Lista vacía')
        if self.orde.get() == 'Burbuja':             # Si el método es "Burbuja" / If sorting method is Bubble sort
            self.lis = list(self.listview.get(0, END))  # Convierte los elementos del Listbox a lista / Converts Listbox to list
            if len(self.lis) == 0:                   # Si la lista está vacía / If list is empty
                messagebox.showerror('Error','Lista vacía')
            else:
                # Algoritmo de ordenamiento burbuja / Bubble sort algorithm
                for i in range(0, len(self.lis)):
                    for x in range(0, len(self.lis)-1):
                        if self.lis[x] > self.lis[x+1]:
                            aux = self.lis[x]
                            self.lis[x] = self.lis[x+1]
                            self.lis[x+1] = aux
                print(self.lis)                      # Muestra la lista ordenada en consola / Prints sorted list in console
                self.listview.delete(0, END)         # Limpia el Listbox / Clears Listbox
                for i in self.lis:                   # Inserta los valores ordenados / Inserts sorted values
                    self.listview.insert(self.listview.size()+1, str(i))
        else:
            # Método de ordenamiento por selección / Selection sort method
            self.lis = list(self.listview.get(0, END))
            if len(self.lis) == 0:
                messagebox.showerror('Error','Lista vacía')
            else:
                self.arreglo = np.array(self.lis)    # Convierte a arreglo NumPy (no esencial aquí) / Converts to NumPy array (not essential)
                p = 0
                for i in range(p, len(self.lis)):
                    aux = self.lis[i]
                    p = i
                    for x in range(i, len(self.lis)):
                        if aux < self.lis[x]:        # Busca el mayor elemento / Finds the largest element
                            aux = self.lis[x]
                            p = x
                    self.lis[p] = self.lis[i]        # Intercambia posiciones / Swaps positions
                    self.lis[i] = str(aux)
                print(self.lis)
                self.listview.delete(0, END)
                for i in self.lis:
                    self.listview.insert(self.listview.size()+1, str(i))

    # ------------------------------------------------------------
    # Método que inicializa la interfaz gráfica / Method that initializes GUI
    # ------------------------------------------------------------
    def inicio(self):
        self.dato = Entry(self.ven)                  # Campo de texto para ingresar números / Entry box for input
        self.dato.place(x=50, y=10)                  # Posiciona el Entry / Places the Entry
        self.modo = StringVar(value='Pilas')         # Variable para el modo de eliminación / Mode variable (Stack or Queue)
        self.orde = StringVar(value='Burbuja')       # Variable para el tipo de ordenamiento / Sorting method variable

        # Botones de selección (modo de estructura) / Radio buttons for mode selection
        Radiobutton(self.ven, text='Pilas', variable=self.modo, value='Pilas').place(x=60, y=100)
        Radiobutton(self.ven, text='Colas', variable=self.modo, value='Colas').place(x=130, y=100)

        # Botones de selección (tipo de ordenamiento) / Radio buttons for sorting method
        Radiobutton(self.ven, text='Ordenar burbuja', variable=self.orde, value='Burbuja').place(x=60, y=150)
        Radiobutton(self.ven, text='Ordenar selección', variable=self.orde, value='Seleccion').place(x=60, y=200)

        # Botones de acción / Action buttons
        Button(self.ven, text="Validar", command=self.validarcaja).place(x=15, y=40)
        Button(self.ven, text='Eliminar', command=self.EliminarDato).place(x=80, y=40)
        Button(self.ven, text='Ordenar', command=self.Ordenar).place(x=150, y=40)

        # Lista donde se muestran los datos / Listbox to display data
        self.listview = Listbox(self.ven, height=10, width=15, bg='grey', activestyle="dotbox", fg="Black")
        self.listview.place(x=250, y=10)

        # Etiqueta que muestra el número de elementos / Label showing number of elements
        self.label = Label(self.ven, text="numero")
        self.label.place(x=55, y=75)

        # Inicia el bucle principal de la ventana / Starts the main window loop
        self.ven.mainloop()

# ------------------------------------------------------------
# Punto de entrada del programa / Program entry point
# ------------------------------------------------------------
if __name__=='__main__':
    app = Principal()    # Crea una instancia de la clase Principal / Creates instance of Principal class
    app.inicio()         # Llama al método que inicia la interfaz / Calls method to start GUI
