# Ejercicio 4

años = int(input('Digite su edad: '))
edad = ''
if años <= 10:
    edad = 'La infancia es increíble y bella'
elif años <= 20:
    edad = 'Tienes muchos cambios, mucho que estudiar'
elif años <= 29:
    edad = 'Amor y comienza el trabajo'
elif años >= 30:
    edad = 'Edad invalida'
else:
    print('Has ingresado una edad no valida')

print(f'Tienes {años} años: {edad}')
