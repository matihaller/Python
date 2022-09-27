# Ejercicio 4

calificacion_promedio = 0
calificacion_baja = 99999
calificacion = 0
suma = 0

for i in range(10):

    calificacion = int(input("Introduce una calificación: "))

    suma += calificacion

    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

    else:
        calificacion_promedio = suma / 10

print("La calificación más baja es:", calificacion_baja,
"\nLa calificación promedio es:", calificacion_promedio)