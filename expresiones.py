import sqlite3

# Conectarse a la base de datos (o crearla si no existe)
conn = sqlite3.connect('mi_diccionario_expresiones.db')

# Crear la tabla 'diccionario' con dos columnas: 'expresiones' y 'definicion'
conn.execute('CREATE TABLE IF NOT EXISTS diccionario (expresion TEXT, definicion TEXT, traduccion TEXT, region TEXT)')

# Agregar algunas expresiones y definiciones
cont=1
while cont!=0:
    expresion=input("Ingrese una nueva expresión: ")
    definicion=input("Definición de la expresión: ")
    traduccion = input("Traducción al inglés: ")
    region = input("Región: ")
    # Convertir la expresión ingresada a minúsculas antes de insertarla en la base de datos
    expresion = expresion.lower()
    conn.execute("INSERT INTO diccionario (expresion, definicion, traduccion, region) VALUES (?, ?, ?, ?)", (expresion, definicion, traduccion, region))
    
    # Guardar los cambios en la base de datos
    conn.commit()