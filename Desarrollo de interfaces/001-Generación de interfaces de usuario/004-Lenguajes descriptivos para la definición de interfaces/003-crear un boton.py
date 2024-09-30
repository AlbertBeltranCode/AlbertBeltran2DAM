import tkinter as tk #Importamos la libreria tkinter para poder trabajar con interfaces

ventana = tk.Tk() #Creamos una ventana mediante la funcion TK()

tk.Button(ventana,text="Pulsame",padx=15,pady=15).pack(padx=40,pady=40) #Creamos un boton dentro de la ventana

ventana.mainloop()  # Inicia la ventana principal