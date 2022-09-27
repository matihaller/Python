# ejercicio 5

califacion = int(input("Ingrese la calificacion: "))
if califacion == 9 or califacion <= 10:
    print("A")
elif califacion == 8:
    print("B")
elif califacion == 7:
    print("C")
elif califacion == 6:
    print("D")
elif califacion == 0 or califacion <= 6:
    print("F")
else: 
    print("Calificacion invalida")