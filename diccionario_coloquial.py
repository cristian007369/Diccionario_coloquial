from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def buscar_palabras_expresiones(evento):
    global busqueda1
    t_resultados_in.config(state="normal")
    t_resultados_es.config(state="normal")
    bt_agregar.config(state="disabled")
    t_resultados_es.delete("1.0","end")
    t_resultados_in.delete("1.0","end")
    busqueda1 = busqueda.get().lower()
    resultado = conn.execute(f"SELECT definicion, traduccion, region FROM diccionario WHERE palabra = '{busqueda1}'").fetchone()
    resultado1 = conn1.execute(f"SELECT definicion, traduccion, region FROM diccionario WHERE expresion = '{busqueda1}'").fetchone()
    if busqueda.get()=="":
        t_resultados_es.insert(INSERT, f"Debes buscar una palabra o expresión")
        t_resultados_in.insert(INSERT, f"You must search for a word or expression")
    elif resultado:
        definicion = resultado[0]
        traduccion = resultado[1]
        region = resultado[2]
        t_resultados_es.insert(INSERT, f"La definición de '{busqueda1}' es:\n")
        t_resultados_es.insert(INSERT, f"{definicion}\n")
        t_resultados_es.insert(INSERT, f"Región a la que pertenece:\n{region}")
        t_resultados_in.insert(INSERT, f"The definition of '{busqueda1}' is:\n")
        t_resultados_in.insert(INSERT, f"{traduccion}\n")
        t_resultados_in.insert(INSERT, f"Region to which it belongs:\n{region}")
    elif resultado1:
        definicion = resultado1[0]
        traduccion = resultado1[1]
        region = resultado1[2]
        t_resultados_es.insert(INSERT, f"La definición de '{busqueda1}' es:\n")
        t_resultados_es.insert(INSERT, f"{definicion}\n")
        t_resultados_es.insert(INSERT, f"Región a la que pertenece:\n{region}")
        t_resultados_in.insert(INSERT, f"The definition of '{busqueda1}' is:\n")
        t_resultados_in.insert(INSERT, f"{traduccion}\n")
        t_resultados_in.insert(INSERT, f"Region to which it belongs:\n{region}")
    else:
        global toplevel_agregar
        t_resultados_es.insert(INSERT, f"No se encontró '{busqueda1}' en el diccionario")
        t_resultados_in.insert(INSERT, f"'{busqueda1}' not found in dictionary")
        
        toplevel_agregar = Toplevel()
        toplevel_agregar.resizable(False, False)
        toplevel_agregar.config(bg="white")
        toplevel_agregar.geometry("230x120")
        
        label_titulo = Label(toplevel_agregar,bg="white",text="¿Deseas agregarla?",font=("times new roman",20))
        label_titulo.place(x=10, y=10)
        
        bt_si = Button(toplevel_agregar,bg="white",text="Sí", command=precionar_si)
        bt_si.place(x=10, y=60, width=100, height=50)

        bt_no = Button(toplevel_agregar,bg="white",text="No", command= precionar_no)
        bt_no.place(x=120, y=60, width=100, height=50)
    t_resultados_in.config(state="disabled")
    t_resultados_es.config(state="disabled")
    entry_busqueda.delete(0, "end")
def ver_base_datos_palabras():
    toplevel_palabras = Toplevel()
    toplevel_palabras.title("Plabras disponibles")
    toplevel_palabras.resizable(False, False)
    toplevel_palabras.geometry("340x340")

    t_resultados = Text(toplevel_palabras)
    t_resultados.config(bg="skyblue1", fg="black", font=("times new roman", 20))
    t_resultados.place(x=0,y=0,width=740,height=340)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diccionario")
    resultados = cursor.fetchall()

    t_resultados.insert(INSERT, f"Palabras:\n")
    for fila in resultados:
        t_resultados.insert(INSERT, f"*{fila[0]}\n")
    t_resultados.config(state="disabled")
def ver_base_datos_expresiones():
    toplevel_palabras = Toplevel()
    toplevel_palabras.title("Expresiones disponibles")
    toplevel_palabras.resizable(False, False)
    toplevel_palabras.geometry("340x340")

    t_resultados = Text(toplevel_palabras)
    t_resultados.config(bg="skyblue1", fg="black", font=("times new roman", 20))
    t_resultados.place(x=0,y=0,width=740,height=340)

    cursor = conn1.cursor()
    cursor.execute("SELECT * FROM diccionario")
    resultados = cursor.fetchall()

    t_resultados.insert(INSERT, f"Expresiones:\n")
    for fila in resultados:
        t_resultados.insert(INSERT, f"*{fila[0]}\n")
    t_resultados.config(state="disabled")
def agregar_nueva(): 
    global toplevel_agregar1
    bt_agregar.config(state="disabled")   
    toplevel_agregar1 = Toplevel()
    toplevel_agregar1.title("Agregar nueva")
    toplevel_agregar1.resizable(False, False)
    toplevel_agregar1.config(bg="white")
    toplevel_agregar1.geometry("230x70")
            
    bt_palabra = Button(toplevel_agregar1,bg="white",text="Palabra", command=agregar_nueva_palabra)
    bt_palabra.place(x=10, y=10, width=100, height=50)

    bt_expresion = Button(toplevel_agregar1,bg="white",text="Expresión", command= agregar_nueva_expresion)
    bt_expresion.place(x=120, y=10, width=100, height=50)
    pass
def precionar_si():
    t_resultados_in.config(state="normal")
    t_resultados_es.config(state="normal")
    t_resultados_es.delete("1.0","end")
    t_resultados_in.delete("1.0","end")
    bt_agregar.config(state="active")
    toplevel_agregar.destroy()
    t_resultados_in.config(state="disabled")
    t_resultados_es.config(state="disabled")
def precionar_no():
    t_resultados_in.config(state="normal")
    t_resultados_es.config(state="normal")
    t_resultados_es.delete("1.0","end")
    t_resultados_in.delete("1.0","end")
    toplevel_agregar.destroy()
    t_resultados_in.config(state="disabled")
    t_resultados_es.config(state="disabled")
def agregar_nueva_palabra():
    global toplevel_agregar2
    toplevel_agregar1.destroy()
    toplevel_agregar2 = Toplevel()
    toplevel_agregar2.title("Nueva palabra")
    toplevel_agregar2.resizable(False, False)
    toplevel_agregar2.config(bg="white")
    toplevel_agregar2.geometry("272x418")

    label_imagen = Label(toplevel_agregar2,bg="white",image=barra_texto)
    label_imagen.place(x=10, y=20)

    text_uno = Text(toplevel_agregar2, bg="white", fg="gray", font=("Times New Roman", 25), bd=0, width=13, height=1)
    text_uno.insert("1.0", f"{busqueda1}")
    text_uno.config(state="disabled")
    text_uno.place(x=25, y=26)

    label_imagen = Label(toplevel_agregar2,bg="white",image=barra_texto)
    label_imagen.place(x=10, y=102)

    entry_definicion = Entry(toplevel_agregar2, textvariable=definicion)
    entry_definicion.config(bg="white", fg="gray", font=("Times New Roman", 19), width=19,bd=0)
    entry_definicion.insert(0, "Definición")
    entry_definicion.bind("<FocusIn>", lambda event: entry_definicion.delete(0, "end") if definicion.get() == "Definición" else None)
    entry_definicion.bind("<Key>",lambda event: entry_definicion.config(fg="Black"))
    entry_definicion.bind("<Return>", lambda event: entry_traducion.focus_set())
    entry_definicion.place(x=25,y=112)

    label_imagen = Label(toplevel_agregar2,bg="white",image=barra_texto)
    label_imagen.place(x=10, y=184)

    entry_traducion = Entry(toplevel_agregar2, textvariable=traducion)
    entry_traducion.config(bg="white", fg="gray", font=("Times New Roman", 19), width=19,bd=0)
    entry_traducion.insert(0, "Traducción")
    entry_traducion.bind("<FocusIn>",lambda event: entry_traducion.delete(0, "end") if traducion.get() == "Traducción" else None)
    entry_traducion.bind("<Key>",lambda event: entry_traducion.config(fg="Black"))
    entry_traducion.bind("<Return>", lambda event: cmb_region.focus_set())
    entry_traducion.place(x=25,y=194)

    cmb_region = ttk.Combobox(toplevel_agregar2, textvariable=region_selected, values=region, font=("times new roman", 20))
    cmb_region.set("Región")
    cmb_region.bind("<FocusIn>", lambda event: cmb_region.event_generate("<Down>") if region_selected.get()=="Región" else None)
    cmb_region.place(x=15, y=270,width=247,height=50)
 
    bt_guardar = Button(toplevel_agregar2,bg="white",text="Guardar", command=guardar_nueva_palabra)
    bt_guardar.config(state="active")
    bt_guardar.place(x=86, y=348, width=100, height=50)
def agregar_nueva_expresion():
    global toplevel_agregar3
    toplevel_agregar1.destroy()
    toplevel_agregar3 = Toplevel()
    toplevel_agregar3.title("Nueva Expresión")
    toplevel_agregar3.resizable(False, False)
    toplevel_agregar3.config(bg="white")
    toplevel_agregar3.geometry("272x418")

    label_imagen = Label(toplevel_agregar3,bg="white",image=barra_texto)
    label_imagen.place(x=10, y=20)

    text_uno = Text(toplevel_agregar3, bg="white", fg="gray", font=("Times New Roman", 25), bd=0, width=13, height=1)
    text_uno.insert("1.0", f"{busqueda1}")
    text_uno.config(state="disabled")
    text_uno.place(x=25, y=26)

    label_imagen = Label(toplevel_agregar3,bg="white",image=barra_texto)
    label_imagen.place(x=10, y=102)

    entry_definicion = Entry(toplevel_agregar3, textvariable=definicion)
    entry_definicion.config(bg="white", fg="gray", font=("Times New Roman", 19), width=19,bd=0)
    entry_definicion.insert(0, "Definición")
    entry_definicion.bind("<FocusIn>", lambda event: entry_definicion.delete(0, "end") if definicion.get() == "Definición" else None)
    entry_definicion.bind("<Key>",lambda event: entry_definicion.config(fg="Black"))
    entry_definicion.bind("<Return>", lambda event: entry_traducion.focus_set())
    entry_definicion.place(x=25,y=112)

    label_imagen = Label(toplevel_agregar3,bg="white",image=barra_texto)
    label_imagen.place(x=10, y=184)

    entry_traducion = Entry(toplevel_agregar3, textvariable=traducion)
    entry_traducion.config(bg="white", fg="gray", font=("Times New Roman", 19), width=19,bd=0)
    entry_traducion.insert(0, "Traducción")
    entry_traducion.bind("<FocusIn>",lambda event: entry_traducion.delete(0, "end") if traducion.get() == "Traducción" else None)
    entry_traducion.bind("<Key>",lambda event: entry_traducion.config(fg="Black"))
    entry_traducion.bind("<Return>", lambda event: cmb_region.focus_set())
    entry_traducion.place(x=25,y=194)

    cmb_region = ttk.Combobox(toplevel_agregar3, textvariable=region_selected, values=region, font=("times new roman", 20))
    cmb_region.set("Región")
    cmb_region.bind("<FocusIn>", lambda event: cmb_region.event_generate("<Down>") if region_selected.get()=="Región" else None)
    cmb_region.place(x=15, y=270,width=247,height=50)
 
    bt_guardar = Button(toplevel_agregar3,bg="white",text="Guardar", command=guardar_nueva_expresion)
    bt_guardar.config(state="active")
    bt_guardar.place(x=86, y=348, width=100, height=50)
def guardar_nueva_palabra():
    if traducion.get()!="" and traducion.get()!="Traducción" and definicion.get()!="" and definicion.get()!="Definición" and region_selected.get()!="Región":
        conn.execute('CREATE TABLE IF NOT EXISTS diccionario (palabra TEXT, definicion TEXT, traduccion TEXT, region TEXT)')
        conn.execute("INSERT INTO diccionario (palabra, definicion, traduccion, region) VALUES (?, ?, ?, ?)", (busqueda1, definicion.get(), traducion.get(), region_selected.get()))
        conn.commit()
        toplevel_agregar2.destroy()
    else:
        messagebox.showinfo(".____.", "No seas estúpido")
def guardar_nueva_expresion():
    if traducion.get()!="" and traducion.get()!="Traducción" and definicion.get()!="" and definicion.get()!="Definición" and region_selected.get()!="Región":
        conn1.execute('CREATE TABLE IF NOT EXISTS diccionario (expresion TEXT, definicion TEXT, traduccion TEXT, region TEXT)')
        conn1.execute("INSERT INTO diccionario (expresion, definicion, traduccion, region) VALUES (?, ?, ?, ?)", (busqueda1, definicion.get(), traducion.get(), region_selected.get()))
        conn1.commit()
        toplevel_agregar3.destroy()
    else:
        messagebox.showinfo(".____.", "No seas estúpido")

ventana_principal = Tk()
ventana_principal.title("Diccionario coloquial")
ventana_principal.geometry("760x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

global t_resultados_es,t_resultados_in,busqueda, conn, conn1, bt_agregar, barra_texto, definicion, traducion, region_selected, region

conn = sqlite3.connect('mi_diccionario_palabras.db')
conn1 = sqlite3.connect('mi_diccionario_expresiones.db')
barra_texto=PhotoImage(file="barra_texto1.png")
barra=PhotoImage(file="barra_busqueda.png")
region=["Caribe", "Pacífico","Orinoquía", "Amazonía", "Andina","Insular"]
region_selected= StringVar()
busqueda = StringVar()
definicion = StringVar()
traducion = StringVar()

label_imagen = Label(ventana_principal,bg="white",image=barra)
label_imagen.place(x=27, y=7)

entry_busqueda = Entry(ventana_principal, textvariable=busqueda)
entry_busqueda.config(bg="white", fg="gray", font=("Times New Roman", 19), width=50,bd=0)
entry_busqueda.insert(0, "Buscar")
entry_busqueda.bind("<FocusIn>",lambda event: entry_busqueda.delete(0, "end"))
entry_busqueda.bind("<Key>",lambda event: entry_busqueda.config(fg="Black"))
entry_busqueda.bind("<Return>", buscar_palabras_expresiones)
entry_busqueda.place(x=77,y=20)

# areas de texto para los resultados
t_resultados_es = Text(ventana_principal)
t_resultados_es.config(bg="white", fg="black", font=("times new roman", 20),state="disabled")
t_resultados_es.place(x=30,y=80,width=350,height=340)

t_resultados_in = Text(ventana_principal)
t_resultados_in.config(bg="white", fg="black", font=("times new roman", 20),state="disabled")
t_resultados_in.place(x=380,y=80,width=350,height=340)

# botones 
bt_palabras = Button(ventana_principal,bg="white",text="Palabras", command=ver_base_datos_palabras)
bt_palabras.place(x=30, y=440, width=150, height=50)

bt_expresiones = Button(ventana_principal,bg="white",text="Expresiones", command=ver_base_datos_expresiones)
bt_expresiones.place(x=305, y=440, width=150, height=50)

bt_agregar = Button(ventana_principal,bg="white",text="Agregar nueva", command=agregar_nueva)
bt_agregar.config(state="disabled")
bt_agregar.place(x=580, y=440, width=150, height=50)

ventana_principal.mainloop()