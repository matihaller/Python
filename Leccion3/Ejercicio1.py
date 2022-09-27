#Ejercicio 1


anio = int(input('Digite el numero de un año: '))
if anio % 4 == 0:
    print('El año que escribiste es bisiesto')
    opcion = input('¿Desea continuar? (s/n) ')
    if opcion == 's':
        año = int(input('Digite el numero de un año: '))
        
else:
    print('el año que escribiste no es bisiesto')
    opcion = input('¿Desea continuar? (s/n) ')
    if opcion == 's':
        año = int(input('Digite el numero de un año: '))
    else:
        print('Gracias por usar el programa')
      




 ''' 
from calendar import isleap

año = int(input("Introduce un año: "))

while True:
 if isleap(año):
    print("El año es bisiesto".format(año))
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "s":
        año = int(input("Introduce un año: "))
    else:
        print("Gracias por usar el programa")
        break

 else:
    print("El año no es bisiesto".format(año))
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "s":
        año = int(input("Introduce un año: "))
    else:
        print("Gracias por usar el programa")
        break
'''