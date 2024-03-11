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

    Button(frame, width=39,pady=7,text='INGRESAR',bg='black',fg='#EBEBEB',border=0,command=signin).place(x=35,y=204)



    root.mainloop()

def homePage():
    home = Toplevel()
    home.title('Login')
    home.geometry('925x500+300+200')
    home.configure(bg="#EBEBEB")
    home.resizable(False, False)

    img = PhotoImage(file='Codigo/img/logo.png')
    img = img.subsample(2)
    label = Label(home, image=img, bg='#EBEBEB')
    label.place(relx=0.3, rely=0.5, anchor=CENTER)

    frame =Frame(home,width=350,height=350,bg="#EBEBEB")
    frame.place(x=480,y=70)


    Button(frame, width=39,pady=7,text='CREAR REGISTRO',bg='#EBEBEB',fg='black',border=0,command=crear_registro).place(x=35,y=80)
    Button(frame, width=39,pady=7,text='BUSCAR REGISTRO',bg='#EBEBEB',fg='black',border=0).place(x=35,y=200)



    home.mainloop()

def crear_registro():
    db, collection = db_conexion.establecer_conexion('app')

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

    ingresarDelito = Tk()
    ingresarDelito.title("Crear Registro")

    #Treeview para mostrar los datos
    data = ttk.Treeview(ingresarDelito, columns=("ID", "Delito", "Fecha", "Victima", "Edad", "Provincia"))
    data.grid(row=1, column=0, columnspan=2)
    data.heading("#0", text="ID")
    data.heading("#1", text="Delito")
    data.heading("#2", text="Fecha")
    data.heading("#3", text="Victima")
    data.heading("#4", text="Edad")
    data.heading("#5", text="Provincia")

    #ID del delito
    Label(ingresarDelito, text="ID de delito").grid(row=2, column=0)
    _id = Entry(ingresarDelito)
    _id.grid(row=2, column=1)

    #Delito
    Label(ingresarDelito, text="Delito").grid(row=3, column=0)
    delitos = ["Asalto", "Homicidio", "Hurto", "Robo", "Robo de vehiculo", "Tacha de vehiculo"]  # Lista de opciones para el dropdown
    delito_combobox = ttk.Combobox(ingresarDelito, values=delitos)
    delito_combobox.grid(row=3, column=1)

    #Fecha
    Label(ingresarDelito, text="Fecha").grid(row=4, column=0)
    fecha = Entry(ingresarDelito)
    fecha.grid(row=4, column=1)

    #Victima
    Label(ingresarDelito, text="Victima").grid(row=5, column=0)
    victimas = ["Edificacion", "Otros", "Persona", "Vehiculo", "Vivienda"]  # Lista de opciones para el dropdown
    victima_combobox = ttk.Combobox(ingresarDelito, values=victimas)
    victima_combobox.grid(row=5, column=1)

    #Edad
    Label(ingresarDelito, text="Edad").grid(row=6, column=0)
    edades = ["Adulto Mayor", "Desconocido", "Mayor de edad", "Menor de edad"]  # Lista de opciones para el dropdown
    edad_combobox = ttk.Combobox(ingresarDelito, values=edades)
    edad_combobox.grid(row=6, column=1)

    #Provincia
    Label(ingresarDelito, text="Provincia").grid(row=7, column=0)
    provincias = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]  # Lista de opciones para el dropdown
    provincia_combobox = ttk.Combobox(ingresarDelito, values=provincias)
    provincia_combobox.grid(row=7, column=1)

    crear = Button(ingresarDelito, text="Crear Registro", command=crearRegistro, bg="black", fg="white")
    crear.grid(row=8, columnspan=2)

    for column in data["columns"]:
        data.column(column, anchor="center")

    mostrarDatos()
    ingresarDelito.mainloop()


inicio_sesion()