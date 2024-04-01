from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db_conexion

def inicio_sesion():
    db, collection = db_conexion.establecer_conexion('usuario')

    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#EBEBEB")
    root.resizable(False, False)

    def signin():
        # Obtener el correo y la contraseña de los campos de entrada
        username = user.get()
        password = code.get()

        # Buscar el usuario en la colección de MongoDB
        user_data = collection.find_one({"correo": username, "contrasena": password})

        # Verificar si se encontró el usuario y si las credenciales son correctas
        if user_data:
            homePage()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Por favor, inténtalo de nuevo.")

        # Limpiar los campos de entrada después de verificar las credenciales
        user.delete(0, 'end')
        code.delete(0, 'end')


    img = PhotoImage(file='Codigo/img/logo.png')
    img = img.subsample(2)
    label = Label(root, image=img, bg='#EBEBEB')
    label.place(relx=0.3, rely=0.5, anchor=CENTER)

    frame =Frame(root,width=350,height=350,bg="#EBEBEB")
    frame.place(x=480,y=70)

    heading = Label(frame, text='INICIAR SESION', fg='black',bg='#EBEBEB',font=('Hatton',23,'bold'))
    heading.place(x=55,y=5)


    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name = user.get()
        if name =='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg="#EBEBEB",font=('Hatton',11))
    user.place(x=30,y=80)
    user.insert(0, "Correo")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2,bg='black').place(x=25,y=107)


    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name = code.get()
        if name =='':
            code.insert(0,'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg="#EBEBEB",font=('Hatton',11))
    code.place(x=30,y=150)
    code.insert(0, "Contra")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)

    Button(frame, width=39,pady=7,text='INGRESAR',bg='black',fg='#EBEBEB',border=0,command=homePage).place(x=35,y=204)


    root.mainloop()

def homePage():
    home = Tk()
    home.title('Home Page')
    home.geometry('925x500+300+200')
    home.configure(bg="#EBEBEB")
    home.resizable(False, False)

    #img = PhotoImage(file='Codigo/img/logo.png')
    #img = img.subsample(2)
    #label = Label(home, image=img, bg='#EBEBEB')
    #label.place(relx=0.3, rely=0.5, anchor=CENTER)

    frame = Frame(home, width=350, height=350, bg="#EBEBEB")
    frame.place(x=480, y=70)

    def crear_registro():
        db, collection = db_conexion.establecer_conexion('app')
        ingresarDelito = Toplevel()
        ingresarDelito.title('Crear Registro')
        ingresarDelito.geometry('1300x670+300+200')
        ingresarDelito.configure(bg="#EBEBEB")
        ingresarDelito.resizable(False, False)

        # Función para mostrar los datos en el Treeview
        def mostrarDatos():
            for documento in collection.find():
                data.insert('', 0, text=documento["_id"], values=(documento["Delito"], documento["Fecha"], documento["Victima"], documento["Edad"], documento["Provincia"]))

        # Función para crear un nuevo registro
        def crearRegistro():
            # Obtener los valores de las entradas de texto
            id_delito = _id.get()
            delito_value = delito_combobox.get()
            fecha_value = fecha.get()
            victima_value = victima_combobox.get()
            edad_value = edad_combobox.get()
            provincia_value = provincia_combobox.get()

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
                
                # Limpiar los campos después de agregar el nuevo registro
                _id.delete(0, END)
                fecha.delete(0, END)
                
                mostrarDatos()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        # Treeview para mostrar los datos
        data = ttk.Treeview(ingresarDelito, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
        data.pack(pady=20, padx=20)
        data.heading("#0", text="ID")
        data.heading("#1", text="Delito")
        data.heading("#2", text="Fecha")
        data.heading("#3", text="Victima")
        data.heading("#4", text="Edad")
        data.heading("#5", text="Provincia")

        # ID del delito
        Label(ingresarDelito, text="ID de delito").pack(pady=(10, 0))
        _id = Entry(ingresarDelito, width=30)
        _id.pack()

        # Delito
        Label(ingresarDelito, text="Delito").pack(pady=(10, 0))
        delitos = ["Asalto", "Homicidio", "Hurto", "Robo", "Robo de vehiculo", "Tacha de vehiculo"]  # Lista de opciones para el dropdown
        delito_combobox = ttk.Combobox(ingresarDelito, values=delitos)
        delito_combobox.pack()

        # Fecha
        Label(ingresarDelito, text="Fecha").pack(pady=(10, 0))
        fecha = Entry(ingresarDelito, width=30)
        fecha.pack()

        # Victima
        Label(ingresarDelito, text="Victima").pack(pady=(10, 0))
        victimas = ["Edificacion", "Otros", "Persona", "Vehiculo", "Vivienda"]  # Lista de opciones para el dropdown
        victima_combobox = ttk.Combobox(ingresarDelito, values=victimas)
        victima_combobox.pack()

        # Edad
        Label(ingresarDelito, text="Edad").pack(pady=(10, 0))
        edades = ["Adulto Mayor", "Desconocido", "Mayor de edad", "Menor de edad"]  # Lista de opciones para el dropdown
        edad_combobox = ttk.Combobox(ingresarDelito, values=edades)
        edad_combobox.pack()

        # Provincia
        Label(ingresarDelito, text="Provincia").pack(pady=(10, 0))
        provincias = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]  # Lista de opciones para el dropdown
        provincia_combobox = ttk.Combobox(ingresarDelito, values=provincias)
        provincia_combobox.pack()

        crear = Button(ingresarDelito, text="Crear Registro", command=crearRegistro, bg="black", fg="white", bd=2, relief="groove")
        crear.pack(pady=10)

        regresar = Button(ingresarDelito, text="Regresar a Inicio", command=ingresarDelito.destroy, bg="black", fg="white", bd=2, relief="groove")
        regresar.pack()

        for column in data["columns"]:
            data.column(column, anchor="center")

        mostrarDatos()
        ingresarDelito.mainloop()

    def eliminar_registro():
        db, collection = db_conexion.establecer_conexion('app')
        eliminarDelito = Toplevel()
        eliminarDelito.title('Eliminar Registro')
        eliminarDelito.geometry('1300x450+300+200')
        eliminarDelito.configure(bg="#EBEBEB")
        eliminarDelito.resizable(False, False)

        # Función para mostrar los datos en el Treeview
        def mostrarDatos():
            for documento in collection.find():
                data.insert('', 0, text=documento["_id"], values=(documento["Delito"], documento["Fecha"], documento["Victima"], documento["Edad"], documento["Provincia"]))

        # Función para eliminar un registro
        def eliminarRegistro():
            id_delito = id_entry.get()
            if id_delito:
                if collection.find_one({"_id": id_delito}):
                    collection.delete_one({"_id": id_delito})
                    messagebox.showinfo("Éxito", f"Registro con ID {id_delito} eliminado exitosamente.")
                    data.delete(*data.get_children())
                    mostrarDatos()
                    id_entry.delete(0, END)
                else:
                    messagebox.showerror("Error", f"No se encontró ningún registro con el ID {id_delito}.")
            else:
                messagebox.showerror("Error", "Por favor, ingrese el ID del registro que desea eliminar.")

        # Treeview para mostrar los datos
        data = ttk.Treeview(eliminarDelito, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
        data.pack(pady=20, padx=20)
        data.heading("#0", text="ID")
        data.heading("#1", text="Delito")
        data.heading("#2", text="Fecha")
        data.heading("#3", text="Victima")
        data.heading("#4", text="Edad")
        data.heading("#5", text="Provincia")

        # ID del delito a eliminar
        Label(eliminarDelito, text="ID del registro a eliminar").pack(pady=(10, 0))
        id_entry = Entry(eliminarDelito, width=30)
        id_entry.pack()

        # Botón para eliminar registro
        eliminar = Button(eliminarDelito, text="Eliminar Registro", command=eliminarRegistro, bg="black", fg="white", bd=2, relief="groove")
        eliminar.pack(pady=10)

        # Botón para regresar a inicio
        regresar = Button(eliminarDelito, text="Regresar a Inicio", command=eliminarDelito.destroy, bg="black", fg="white", bd=2, relief="groove")
        regresar.pack()

        # Alinear columnas en el Treeview al centro
        for column in data["columns"]:
            data.column(column, anchor="center")

        # Mostrar los datos en el Treeview
        mostrarDatos()

        eliminarDelito.mainloop()

    def actualizar_registro():
        db, collection = db_conexion.establecer_conexion('app')
        actualizarDelito = Toplevel()
        actualizarDelito.title('Actualizar Registro')
        actualizarDelito.geometry('1300x670+300+200')
        actualizarDelito.configure(bg="#EBEBEB")
        actualizarDelito.resizable(False, False)

        # Función para mostrar los datos en el Treeview
        def mostrarDatos():
            for documento in collection.find():
                data.insert('', 0, text=documento["_id"], values=(documento["Delito"], documento["Fecha"], documento["Victima"], documento["Edad"], documento["Provincia"]))

        # Función para actualizar un registro
        def actualizarRegistro():
            # Obtener los valores de las entradas de texto
            id_delito = _id.get()
            delito_value = delito_combobox.get()
            fecha_value = fecha.get()
            victima_value = victima_combobox.get()
            edad_value = edad_combobox.get()
            provincia_value = provincia_combobox.get()

            # Verificar que se haya proporcionado un ID de delito
            if len(id_delito) != 0:
                # Verificar si el registro con el ID proporcionado existe en la base de datos
                if collection.find_one({"_id": id_delito}):
                    # Crear un diccionario con los campos que se desean actualizar
                    campos_actualizados = {}

                    # Actualizar campos solo si se proporcionan valores
                    if len(delito_value) != 0:
                        campos_actualizados["Delito"] = delito_value
                    if len(fecha_value) != 0:
                        campos_actualizados["Fecha"] = fecha_value
                    if len(victima_value) != 0:
                        campos_actualizados["Victima"] = victima_value
                    if len(edad_value) != 0:
                        campos_actualizados["Edad"] = edad_value
                    if len(provincia_value) != 0:
                        campos_actualizados["Provincia"] = provincia_value

                    # Actualizar el registro en la base de datos
                    collection.update_one({"_id": id_delito}, {"$set": campos_actualizados})

                    messagebox.showinfo("Éxito", f"Registro con ID {id_delito} actualizado exitosamente.")
                else:
                    messagebox.showerror("Error", f"No se encontró ningún registro con el ID {id_delito}.")
            else:
                messagebox.showerror("Error", "Por favor, ingrese el ID del registro que desea actualizar.")

        # Treeview para mostrar los datos
        data = ttk.Treeview(actualizarDelito, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
        data.pack(pady=20, padx=20)
        data.heading("#0", text="ID")
        data.heading("#1", text="Delito")
        data.heading("#2", text="Fecha")
        data.heading("#3", text="Victima")
        data.heading("#4", text="Edad")
        data.heading("#5", text="Provincia")

        # ID del delito a actualizar
        Label(actualizarDelito, text="ID del registro a actualizar").pack(pady=(10, 0))
        _id = Entry(actualizarDelito, width=30)
        _id.pack()

        # Delito
        Label(actualizarDelito, text="Delito").pack(pady=(10, 0))
        delitos = ["Asalto", "Homicidio", "Hurto", "Robo", "Robo de vehiculo", "Tacha de vehiculo"]  # Lista de opciones para el dropdown
        delito_combobox = ttk.Combobox(actualizarDelito, values=delitos)
        delito_combobox.pack()

        # Fecha
        Label(actualizarDelito, text="Fecha").pack(pady=(10, 0))
        fecha = Entry(actualizarDelito, width=30)
        fecha.pack()

        # Victima
        Label(actualizarDelito, text="Victima").pack(pady=(10, 0))
        victimas = ["Edificacion", "Otros", "Persona", "Vehiculo", "Vivienda"]  # Lista de opciones para el dropdown
        victima_combobox = ttk.Combobox(actualizarDelito, values=victimas)
        victima_combobox.pack()

        # Edad
        Label(actualizarDelito, text="Edad").pack(pady=(10, 0))
        edades = ["Adulto Mayor", "Desconocido", "Mayor de edad", "Menor de edad"]  # Lista de opciones para el dropdown
        edad_combobox = ttk.Combobox(actualizarDelito, values=edades)
        edad_combobox.pack()

        # Provincia
        Label(actualizarDelito, text="Provincia").pack(pady=(10, 0))
        provincias = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]  # Lista de opciones para el dropdown
        provincia_combobox = ttk.Combobox(actualizarDelito, values=provincias)
        provincia_combobox.pack()

        actualizar = Button(actualizarDelito, text="Actualizar Registro", command=actualizarRegistro, bg="black", fg="white", bd=2, relief="groove")
        actualizar.pack(pady=10)

        regresar = Button(actualizarDelito, text="Regresar a Inicio", command=actualizarDelito.destroy, bg="black", fg="white", bd=2, relief="groove")
        regresar.pack()

        for column in data["columns"]:
            data.column(column, anchor="center")

        mostrarDatos()
        actualizarDelito.mainloop()

    def buscar_registro():
        db, collection = db_conexion.establecer_conexion('app')
        buscarDelito = Toplevel()
        buscarDelito.title('Buscar Registro')
        buscarDelito.geometry('1300x450+300+200')
        buscarDelito.configure(bg="#EBEBEB")
        buscarDelito.resizable(False, False)

        # Función para mostrar los datos en el Treeview
        def mostrarDatos():
            id_delito = id_entry.get()
            if id_delito:
                for documento in collection.find({"_id": id_delito}):
                    data.insert('', 0, text=documento["_id"], values=(documento["Delito"], documento["Fecha"], documento["Victima"], documento["Edad"], documento["Provincia"]))

        # Treeview para mostrar los datos
        data = ttk.Treeview(buscarDelito, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
        data.pack(pady=20, padx=20)
        data.heading("#0", text="ID")
        data.heading("#1", text="Delito")
        data.heading("#2", text="Fecha")
        data.heading("#3", text="Victima")
        data.heading("#4", text="Edad")
        data.heading("#5", text="Provincia")

        # ID del delito a buscar
        Label(buscarDelito, text="ID del registro a buscar").pack(pady=(10, 0))
        id_entry = Entry(buscarDelito, width=30)
        id_entry.pack()

        # Botón para buscar registro
        buscar = Button(buscarDelito, text="Buscar Registro", command=mostrarDatos, bg="black", fg="white", bd=2, relief="groove")
        buscar.pack(pady=10)

        # Botón para regresar a inicio
        regresar = Button(buscarDelito, text="Regresar a Inicio", command=buscarDelito.destroy, bg="black", fg="white", bd=2, relief="groove")
        regresar.pack()

        # Alinear columnas en el Treeview al centro
        for column in data["columns"]:
            data.column(column, anchor="center")

        buscarDelito.mainloop()

    Button(frame, text='Buscar Registro', bg='#EBEBEB', fg='black', bd=2, relief="groove", command=buscar_registro).place(relx=0.5, rely=0.1, anchor=CENTER)
    Button(frame, text='Crear Registro', bg='#EBEBEB', fg='black', bd=2, relief="groove", command=crear_registro).place(relx=0.5, rely=0.3, anchor=CENTER)
    Button(frame, text='Eliminar Registro', bg='#EBEBEB', fg='black', bd=2, relief="groove", command=eliminar_registro).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(frame, text='Actualizar Registro', bg='#EBEBEB', fg='black', bd=2, relief="groove", command=actualizar_registro).place(relx=0.5, rely=0.7, anchor=CENTER)

    home.mainloop()


inicio_sesion()