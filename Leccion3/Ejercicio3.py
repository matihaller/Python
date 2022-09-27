#Ejercicio 3

conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0

for i in range(10):

    num = int(input("Introduce un número: "))
    
    if num > 0:
        conteo_positivos += 1
    elif num < 0:
        conteo_negativos += 1
    else:
        conteo_neutros += 1
        
print("La cantidad de numeros positivos es:", conteo_positivos,
        "\nLa cantidad de numeros negativos es:", conteo_negativos,
        "\nLa cantidad de numeros neutros es:", conteo_neutros)



