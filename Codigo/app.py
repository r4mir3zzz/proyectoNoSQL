import db_conexion
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


db, collection = db_conexion.establecer_conexion('app')
# Muestra los documentos de la base de datos en consola
"""for documento in collection.find():
    print(documento)"""

def mostrarDatos():
    for documento in collection.find():
        data.insert('', 0, text=documento["_id"], values=(documento["Delito"], documento["Fecha"], documento["Victima"], documento["Edad"], documento["Provincia"]))


root = Tk()
data = ttk.Treeview(root, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
data.grid(row=1, column=0, columnspan=2)
data.heading("#0", text="ID")
data.heading("#1", text="Delito")
data.heading("#2", text="Fecha")
data.heading("#3", text="Victima")
data.heading("#4", text="Edad")
data.heading("#5", text="Provincia")


for column in data["columns"]:
    data.column(column, anchor="center")



mostrarDatos()
root.mainloop()