import sqlite3

# Conectarse a la base de datos (o crearla si no existe)
conn = sqlite3.connect('mi_diccionario_expresiones.db')

# Crear la tabla 'diccionario' con dos columnas: 'palabra' y 'definicion'
conn.execute('CREATE TABLE IF NOT EXISTS diccionario (palabra TEXT, definicion TEXT)')

# Agregar algunas palabras y definiciones
cont=1
while cont!=0:
    expresion=input("Ingrese una nueva expresión: ")
    definicion=input("Definición de la palabra: ")
    conn.execute("INSERT INTO diccionario (palabra, definicion) VALUES (?, ?)", (expresion, definicion))
    # Guardar los cambios en la base de datos
    conn.commit()