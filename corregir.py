import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('mi_diccionario_palabras.db')
cursor = conn.cursor()

# Especificar la columna y el valor en la cláusula WHERE
columna = "palabra"
valor = input("Eliminar: ")

# Ejecutar la sentencia DELETE para eliminar la fila
cursor.execute("DELETE FROM diccionario WHERE {} = ?".format(columna), (valor,))

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión
conn.close()
