from tkinter import *
from tkinter import messagebox
import db_conexion

def inicio_sesion():
    db, collection = db_conexion.establecer_conexion('usuario')

    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
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
    label = Label(root, image=img, bg='white')
    label.place(relx=0.3, rely=0.5, anchor=CENTER)

    frame =Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading = Label(frame, text='INICIAR SESION', fg='#57a1f8',bg='white',font=('Hatton',23,'bold'))
    heading.place(x=80,y=5)


    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name = user.get()
        if name =='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Hatton',11))
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

    code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Hatton',11))
    code.place(x=30,y=150)
    code.insert(0, "Contra")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)

    Button(frame, width=39,pady=7,text='INGRESAR',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)



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


    Button(frame, width=39,pady=7,text='CREAR REGISTRO',bg='#EBEBEB',fg='black',border=0).place(x=35,y=80)
    Button(frame, width=39,pady=7,text='BUSCAR REGISTRO',bg='#EBEBEB',fg='black',border=0).place(x=35,y=200)



    home.mainloop()

inicio_sesion()