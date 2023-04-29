import sqlite3

# Conectar a las base de datos
conn = sqlite3.connect('mi_diccionario_expresiones.db')
conn1 = sqlite3.connect('mi_diccionario_palabras.db')
n=int(input("consultar base de datos\n"))
if n==0:
    # Crear un cursor
    cursor = conn.cursor()
    # Ejecutar una consulta SQL
    cursor.execute("SELECT * FROM diccionario")
    # Obtener los resultados
    resultados = cursor.fetchall()
    # Mostrar los resultados
    for fila in resultados:
        print(fila)
else:
    # Crear un cursor
    cursor1 = conn1.cursor()
    # Ejecutar una consulta SQL
    cursor1.execute("SELECT * FROM diccionario")
    # Obtener los resultados
    resultados = cursor1.fetchall()
    # Mostrar los resultados
    for fila in resultados:
        print(fila)
# Cerrar la conexión
conn.close()
conn1.close()