from tkinter import *
from tkinter import messagebox
def saludar():
    nombre = txt_nombre.get()
    print(f'Hola, {nombre}!!')
    messagebox.showinfo('Saludo', f'Hola, {nombre}')
app = Tk()

app.title('Mi primera aplicación con Tkinter')
app.geometry('400x300')

frame = Frame(app)
frame.grid(row=0,column=0,padx=20,pady=20)
lb_nombre = Label(frame,text='Nombre: ')
lb_nombre.grid(row=0,column=0)
txt_nombre = Entry(frame)
txt_nombre.grid(row=0, column=1)
btn_saludar = Button(frame, text='Saludar', command= saludar)
btn_saludar.grid(row=1,column=0)
app.mainloop()