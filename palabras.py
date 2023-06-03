import sqlite3

# Nos conectamos a la base de datos (o crearla en su defecto)
conn = sqlite3.connect('mi_diccionario_palabras.db')

# Creamos la tabla 'diccionario' con cuatro columnas: 'palabra', 'definicion', 'traduccion' y 'region'
conn.execute('CREATE TABLE IF NOT EXISTS diccionario (palabra TEXT, definicion TEXT, traduccion TEXT, region TEXT)')

# Adregamos palabras con sus definiciones, tradución y región a la pertenece
while True:
    palabra=input("Ingrese una nueva palabra: ").lower()
    resultado = conn.execute(f"SELECT definicion, traduccion, region FROM diccionario WHERE palabra = '{palabra}'").fetchone()
    if resultado:
        None
    else:
        definicion=input("Definición de la palabra: ")
        traduccion = input("Traducción al inglés: ")
        region = input("Región: ")
    
        # Se insertan los nuevos cambios a la tabla 'diccionario'
        conn.execute("INSERT INTO diccionario (palabra, definicion, traduccion, region) VALUES (?, ?, ?, ?)", (palabra, definicion, traduccion, region))
    
        # Guardar los cambios en la base de datos
        conn.commit()
