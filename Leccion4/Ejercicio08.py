# Ejercicio 8: menú interactivo - cajero automático
# hacer un programa que simule un cajero automatico
# con un saldo inicial de $1000 y tendra el sig. menú
# de opciones:
#               1. Ingresar dinero en la cuenta
#               2. Retirar dinero de la cuenta
#               3. Mostrar dinero disponible
#               4. Salir

from pickle import TRUE


saldo = 1000

while True:
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Digite un número: '))
    print()
    if opcion == 1:
        entra = float(input('Ingrese la cantidad de dinero: $'))
        saldo += entra
        print(f'Dinero en la cuenta: ${saldo}')
    elif opcion == 2:
        sale = float(input('Ingrese la cifra de dinero a retirar: $'))
        if sale > saldo:
            print('No tiene esa cantidad de dinero')
        else:
            saldo -= sale
            print(f'Dinero en la cuenta: ${saldo}')
    elif opcion == 3:
        print(f'Tiene un total de ${saldo}')
    elif opcion == 4:
        print("Gracias por usar su cajero")
        break
    else: 
        print('Error, número equivocado.')
        print() 
