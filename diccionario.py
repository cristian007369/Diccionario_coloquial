# Diccionario de palabras coloquiales o expresiones nativas

cerrar=0
while cerrar!=1:
    busqueda=int(input("Dígite 1 para buscar el significado de una palabra o 2 para buscar el de una expresión: "))
    if busqueda==1:
        palabra=0
        while palabra!=2:
            from palabras import *
            palabra=str(input("Dígite 1 para buscar otra palabra: "))
    elif busqueda==2:
        expresión=0
        while expresión!=2:
            from expresiones import *
            expresión=str(input("Dígite 1 para buscar otra expresión: "))
    else:
        print("Entrada no valida")
   
    cerrar=int(input("¿Quieres cerrar el progrma? 1=si, otro número=no: "))
