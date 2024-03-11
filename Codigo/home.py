from tkinter import *

def homePage():
    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#EBEBEB")
    root.resizable(False, False)

    img = PhotoImage(file='img/logo.png')
    img = img.subsample(2)
    label = Label(root, image=img, bg='#EBEBEB')
    label.place(relx=0.3, rely=0.5, anchor=CENTER)

    frame =Frame(root,width=350,height=350,bg="#EBEBEB")
    frame.place(x=480,y=70)


    Button(frame, width=39,pady=7,text='CREAR REGISTRO',bg='#EBEBEB',fg='black',border=0).place(x=35,y=80)
    Button(frame, width=39,pady=7,text='BUSCAR REGISTRO',bg='#EBEBEB',fg='black',border=0).place(x=35,y=200)



    root.mainloop()
homePage()