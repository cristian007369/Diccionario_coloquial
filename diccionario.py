import sqlite3

# Conectarse a la base de datos (o crearla si no existe)
conn = sqlite3.connect('mi_diccionario_palabras.db')
conn1 = sqlite3.connect('mi_diccionario_expresiones.db')

cont=0

while cont!=3:
    cont=int(input("0: palabras o 1: expresiones  "))
    print("-"*50)
    # Consultar la definición de una palabra
    while cont==0:
        palabra_buscar = input("Buscar: ")
        palabra_buscar = palabra_buscar.lower()
        resultado = conn.execute(f"SELECT definicion, traduccion, region FROM diccionario WHERE palabra = '{palabra_buscar}'").fetchone()
        if resultado:
            definicion = resultado[0]
            traduccion = resultado[1]
            region = resultado[2]
            print("-"*50)
            print(f"La definición de '{palabra_buscar}' es: {definicion}")
            print(f"Traducción al inglés: {traduccion}")
            print(f"Región: {region}")
            print("-"*50)
        else:
            print("-"*50)
            print(f"No se encontró la palabra '{palabra_buscar}' en el diccionario")
            print("-"*50)
    
        break

    # Consultar la definición de una expresión 
    while cont==1:
        expresion_buscar = input("Buscar: ")
        expresion_buscar = expresion_buscar.lower()
        resultado = conn1.execute(f"SELECT definicion, traduccion, region FROM diccionario WHERE expresion = '{expresion_buscar}'").fetchone()
        if resultado:
            definicion = resultado[0]
            traduccion = resultado[1]
            region = resultado[2]
            print("-"*50)
            print(f"La definición de '{expresion_buscar}' es: {definicion}")
            print(f"Traducción al inglés: {traduccion}")
            print(f"Región: {region}")
            print("-"*50)
        else:
            print("-"*50)
            print(f"No se encontró la expresión '{expresion_buscar}' en el diccionario")
            print("-"*50)
    
        break

# Cerrar la conexión a la base de datos
conn.close()
conn1.close()
