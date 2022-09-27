# EJERCICIO: Tienda de libros

print("Ingrese los datos del libro ")
nombreLibro = input("Digite el nombre del libro: ")
idLibro = int(input("Digite el id del libro: "))
precio = float(input("Digite el precio del libro: "))
envio = input("Indicar si el envío es gratuito (True/False): ")
if envio == 'true':
    envio = True
elif envio == 'false':
    envio = False
else:
    envio = "el valor digitado es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombreLibro}
        id: {idLibro}
        Precio: ${precio}
        Envio gratuito: {envio}
        ''')