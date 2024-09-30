import tkinter as tk #Importamos la libreria tkinter para poder trabajar con interfaces

ventana = tk.Tk() #Creamos una ventana mediante la funcion TK()

def diHola(): #Definimos la funcion diHola, dicha funcion hace un print del texto Hola
    print("Hola")

tk.Button(ventana,text="Pulsame",padx=15,pady=15,command=diHola).pack(padx=40,pady=40) #Creamos un boton dentro de la ventana y le asignamos la funcion diHola cuando le damos click

ventana.mainloop()  # Inicia la ventana principal
