# ejercicio 3

mes = int(input('Digite el numero de un mes: '))
mesTexto = ''
if mes == 1 or mes == 2 or 3 == mes:
    mesTexto = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    mesTexto = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    mesTexto = 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    mesTexto = 'Primavera'
else:
    print('Has ingresado un numero no valido')

print(f'El més N° {mes} es {mesTexto}')
