#Ejercicio 5: Convertidor de temperaturas 
# Realizar dos funciones para convertir de grados 
# celsius a fahrenheit y viceversa. 
# Investigar las formulas.
# De ºC a ºF: se multiplica por 1.8 y se suma 32.
# De ºF a ºC: se resta 32 y se divide entre 1.8.

temperatura_fahrenheit = float(input('Digite la temperatura en °F: '))
fahrenheit = (temperatura_fahrenheit - 32) / 1.8
print(f'Temperatura en fahrenheit: °{fahrenheit}')

temperatura_fahrenheit = float(input('Digite la temperatura en °C: '))
celsius = (temperatura_fahrenheit * 1.8 + 32)
print(f'Temperatura en celsius: °{celsius}')

'''
#Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #la presedencia: multiplicacion, division y suma

#Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # respetar la presedencia utilizando parentesis

celsius = float(input('Digite el valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado}')
'''