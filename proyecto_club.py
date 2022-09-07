from platform import java_ver
from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import MySQLdb
from turtle import heading, title

master = Tk()
master.title("Proyecto Python")
master.geometry("682x350")

var_id = StringVar()
var_nombre = StringVar()
var_apellido = StringVar()
var_dni = IntVar()
var_telefono = StringVar()
var_email = StringVar()
var_direccion = StringVar()


#conexión con bd
mi_conexion = MySQLdb.connect(host="localhost", user="root", password="", db="bbdd_club")
mi_cursor = mi_conexion.cursor()
mi_cursor.execute("SELECT * FROM socio")
datos = mi_cursor.fetchall()
mi_cursor.close()
mi_conexion.close()



def salir_aplicacion() :
    valor = messagebox.askquestion("Salir", "¿Est+as seguro de que deseas salir de la Aplicación?")
    if valor == "yes" :
        master.destroy()

def limpiar_campos() :
    var_nombre.set("")
    var_apellido.set("")
    var_dni.set("")
    var_telefono.set("")
    var_email.set("")
    var_direccion.set("")
    var_estado_de_cuenta.set("")

def mensaje() :
    acerca = """ 
    Aplicación CRUD 
    Versión 1.0
    Tecnología Python Tkinter
    Autora: Carolina Pettinaroli
    """
    messagebox.showinfo(title="INFORMACIÓN", message=acerca)

################ Métodos CRUD #################
def update() :
    mi_conexion = MySQLdb.connect(host="localhost", user="root", password="", db="bbdd_club")
    try : 
        datos = var_nombre.get(), var_apellido.get(), var_dni.get(), var_telefono.get(), var_email.get(), var_direccion.get(), var_estado_de_cuenta.get()
        mi_cursor.execute("UPDATE socio SET NOMBRE=?, APELLIDO=?, DNI=?, TELEFONO=?, EMAIL=?, DIRECCION=?, ESTADO_DE_CUENTA=? WHERE ID="+var_id.get(), (datos))
        mi_conexion.commit()
    except :
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un Error al actualizar el registro")
        pass
    limpiar_campos()
    mostrar()

def borrar() :
    mi_conexion = MySQLdb.connect(host="localhost", user="root", password="", db="bbdd_club")
    try :
        if messagebox.askyesno("ADVERTENCIA", "¿Realmente desea eliminar el registro?") :
            mi_cursor.execute("DELETE FROM socio WHERE ID="+var_id.get())
            mi_conexion.commit() #para cerrar la instrucción
    except :
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al intentar eliminar el registro")
    limpiar_campos()
    mostrar()


def mostrar() :
    mi_conexion = MySQLdb.connect(host="localhost", user="root", password="", db="bbdd_club")
    mi_cursor = mi_conexion.cursor() 
    registros=tree.get_children()
    for elemento in registros :
        tree.delete(elemento) #para no duplicar valores, sólo en la ventana
    try :
        mi_cursor.execute("SELECT * FROM socio")
        for row in mi_cursor :
            tree.insert("",0,text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    except :
        pass



def create() :
    mi_conexion = MySQLdb.connect(host="localhost", user="root", password="")
    mi_cursor = mi_conexion.cursor()
    try :
        datos = var_nombre.get(), var_apellido.get(), var_dni.get(), var_telefono.get(), var_email.get(), var_direccion.get(), var_estado_de_cuenta.get()
        mi_cursor.execute("INSERT INTO socio VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", (datos))
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un Error al crear el registro. Verifique la conexión con la Base de Datos")
        pass
    limpiar_campos()
    mostrar()

#################################### WIDGETS DE VISTA ################################################
menubar = Menu(master)
menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(label="Salir", command=salir_aplicacion)

menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiar_campos)
ayudamenu.add_command(label="Acerca", command=mensaje)

menubar.add_cascade(label="Ayuda", menu=ayudamenu)

master.config(menu=menubar)


titulo = Label(master, text="ADMINISTRACIÓN DE SOCIOS")
titulo.grid(row=0, column=1)

nombre = Label(master, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)
apellido = Label(master, text="Apellido")
apellido.grid(row=2, column=0, sticky=W)
dni = Label(master, text="DNI")
dni.grid(row=3, column=0, sticky=W)
telefono = Label(master, text="Telefono")
telefono.grid(row=4, column=0, sticky=W)
email = Label(master, text="Email")
email.grid(row=5, column=0, sticky=W)
direccion = Label(master, text="Direccion")
direccion.grid(row=6, column=0, sticky=W)
estado_de_cuenta = Label(master, text="Estado de cuenta")
estado_de_cuenta.grid(row=7, column=0, sticky=W)

entry_nombre = Entry(master, textvariable=var_nombre)
entry_nombre.grid(row=1, column=1)
entry_apellido = Entry(master, textvariable=var_apellido)
entry_apellido.grid(row=2, column=1)
entry_dni = Entry(master, textvariable=var_dni)
entry_dni.grid(row=3, column=1)
entry_telefono = Entry(master, textvariable=var_telefono)
entry_telefono.grid(row=4, column=1)
entry_email = Entry(master, textvariable=var_email)
entry_email.grid(row=5, column=1)
entry_direccion = Entry(master, textvariable=var_direccion)
entry_direccion.grid(row=6, column=1)
entry_estado_de_cuenta = Entry(master, textvariable=var_estado_de_cuenta)
entry_estado_de_cuenta.grid(row=7, column=1)


btn_guardar = Button(master, text="Guardar", command=create)
btn_actualizar = Button(master, text="Actualizar", command=update)
btn_eliminar = Button(master, text="Eliminar", command=borrar)
btn_mostrar = Button(master, text="Mostrar Lista", command=mostrar)

btn_guardar.grid(row=2, column=2)
btn_actualizar.grid(row=4, column=2)
btn_eliminar.grid(row=2, column=3)
btn_mostrar.grid(row=4, column=3)

tree = ttk.Treeview(master) #declaro el tree
tree["columns"] = ("Nombre","Apellido", "DNI", "Teléfono", "Email", "Dirección", "Estado de Cuenta")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("Nombre", width=80, minwidth=80, anchor=W)
tree.column("Apellido", width=80, minwidth=80, anchor=W)
tree.column("DNI", width=80, minwidth=80, anchor=W)
tree.column("Teléfono", width=80, minwidth=80, anchor=W)
tree.column("Email", width=80, minwidth=80, anchor=W)
tree.column("Dirección", width=80, minwidth=80, anchor=W)
tree.column("Estado de Cuenta", width=100, minwidth=100, anchor=W)
tree.heading("#0", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")
tree.heading("DNI", text="DNI")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Email", text="Email")
tree.heading("Dirección", text="Dirección")
tree.heading("Estado de Cuenta", text="Estado de Cuenta")
tree.grid(column=0, row=10, columnspan=9)

def seleccionar_usando_click(event) :
    item=tree.identify('item', event.x, event.y)
    var_id.set(tree.item(item,"text"))
    var_nombre.set(tree.item(item,"values")[0])
    var_apellido.set(tree.item(item,"values")[1])
    var_dni.set(tree.item(item,"values")[2])
    var_telefono.set(tree.item(item,"values")[3])
    var_email.set(tree.item(item,"values")[4])
    var_direccion.set(tree.item(item,"values")[5])
    var_estado_de_cuenta.set(tree.item(item,"values")[6])

tree.bind("<Double-1>", seleccionar_usando_click)


master.mainloop()