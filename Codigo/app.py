import db_conexion
from tkinter import *
db, collection = db_conexion.establecer_conexion()

root = Tk()


# Muestra los documentos de la base de datos en consola
"""for documento in collection.find():
    print(documento)"""






root.mainloop()