# Ejercicio 11: Agenda telefonica. 
# Hacer un programa que simule una agenda de contactos. 
# Crear un diccionario donde la clave sea el nombre del 
# usuario y el valor sea el telefono, el programa tendrá 
# el siguiente menú de opciones.
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir
agenda = {}
while True:
    print('\t.:MENÚ:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = (int(input('Digite una opción: ')))
    if opcion == 1:
        nombre = input('Nombre de contacto: ')
        telefono = input('Número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado.')
        else:
                print('Este contacto ya existe')
    elif opcion == 2:
        nombre = input('Nombre del cotacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Contacto eliminado.')
        else:
            print('Este contacto no existe.')
    elif opcion == 3:
        print(f'\n\tLista de contactos:')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Salir.')
        break
    else:
        print('Opción no válida.')
        print()


