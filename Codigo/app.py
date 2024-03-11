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

def crearRegistro():
    # Obtener los valores de las entradas de texto
    id_delito = _id.get()
    delito_value = delito.get()
    fecha_value = fecha.get()
    victima_value = victima.get()
    edad_value = edad.get()
    provincia_value = provincia.get()

    # Verificar que todos los campos estén llenos
    if len(id_delito) != 0 and len(delito_value) != 0 and len(fecha_value) != 0 and len(victima_value) != 0 and len(edad_value) != 0 and len(provincia_value) != 0:
        # Limpiar la vista de la tabla
        data.delete(*data.get_children())
        
        # Crear un diccionario con los datos del nuevo documento
        nuevo_documento = {
            "_id": id_delito,
            "Delito": delito_value,
            "Fecha": fecha_value,
            "Victima": victima_value,
            "Edad": edad_value,
            "Provincia": provincia_value
        }
       
        collection.insert_one(nuevo_documento)
        
        
        _id.delete(0, END)
        delito.delete(0, END)
        fecha.delete(0, END)
        victima.delete(0, END)
        edad.delete(0, END)
        provincia.delete(0, END)

        
        mostrarDatos()
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

root = Tk()
data = ttk.Treeview(root, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
data.grid(row=1, column=0, columnspan=2)
data.heading("#0", text="ID")
data.heading("#1", text="Delito")
data.heading("#2", text="Fecha")
data.heading("#3", text="Victima")
data.heading("#4", text="Edad")
data.heading("#5", text="Provincia")



#Nombre
Label(root,text="ID de delito").grid(row=2,column=0)
_id=Entry(root)
_id.grid(row=2,column=1)
#Delito
Label(root,text="Delito").grid(row=3,column=0)
delito=Entry(root)
delito.grid(row=3,column=1)
#Fecha
Label(root,text="Fecha").grid(row=4,column=0)
fecha=Entry(root)
fecha.grid(row=4,column=1)
#Victima
Label(root,text="Victima").grid(row=5,column=0)
victima=Entry(root)
victima.grid(row=5,column=1)
#Edad
Label(root,text="Edad").grid(row=6,column=0)
edad=Entry(root)
edad.grid(row=6,column=1)
#Provincia
Label(root,text="Provincia").grid(row=7,column=0)
provincia=Entry(root)
provincia.grid(row=7,column=1)
#Boton crear
crear=Button(root,text="Crear Registro",command=crearRegistro,bg="black",fg="white")
crear.grid(row=8,columnspan=2)


for column in data["columns"]:
    data.column(column, anchor="center")



mostrarDatos()
root.mainloop()