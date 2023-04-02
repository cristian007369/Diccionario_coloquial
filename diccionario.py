import sqlite3

# Conectarse a la base de datos (o crearla si no existe)
conn = sqlite3.connect('mi_diccionario_palabras.db')

# Consultar la definición de una palabra
palabra_buscar = input("Buscar: ")
definicion = conn.execute(f"SELECT definicion FROM diccionario WHERE palabra = '{palabra_buscar}'").fetchone()
if definicion:
    print(f"La definición de '{palabra_buscar}' es: {definicion[0]}")
else:
    print(f"No se encontró la palabra '{palabra_buscar}' en el diccionario")
    
# Cerrar la conexión a la base de datos
conn.close()
