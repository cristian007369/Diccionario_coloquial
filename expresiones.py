import sqlite3

# Nos conectamos a la base de datos (o crearla en su defecto)
conn = sqlite3.connect('mi_diccionario_expresiones.db')

# Creamos la tabla 'diccionario' con cuatro columnas: 'palabra', 'definicion', 'traduccion' y 'region'
conn.execute('CREATE TABLE IF NOT EXISTS diccionario (expresion TEXT, definicion TEXT, traduccion TEXT, region TEXT)')

# Adregamos expresiones con sus definiciones, tradución y región a la pertenece
while True:
    expresion=input("Ingrese una nueva expresión: ").lower()
    resultado = conn.execute(f"SELECT definicion, traduccion, region FROM diccionario WHERE expresion = '{expresion}'").fetchone()
    if resultado:
        None
    else:
        definicion=input("Definición de la expresión: ")
        traduccion = input("Traducción al inglés: ")
        region = input("Región: ")
    
        # Se insertan los nuevos cambios a la tabla 'diccionario'
        conn.execute("INSERT INTO diccionario (expresion, definicion, traduccion, region) VALUES (?, ?, ?, ?)", (expresion, definicion, traduccion, region))
    
        # Guardar los cambios en la base de datos
        conn.commit()