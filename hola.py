#en phyton no uso int float, uso, edad, altura=; no declaras el tipo
#lo deduce el valor, no hay; una misma variable puede cambiar de tipo x=5 x="hola"
#para saber el tipo de un dato print(type(variable))
#Imput siempre devuelve texto,edad = int(input("Edad: "))print(edad + 1)




nombre = input("Ingresa tu nombre ")

try:
        anio = int(input ("Año de nacimiento:"))
        anios =2026-anio
        print (f"Nombre: {nombre} , tiene aproximadamente {anios} años.")
except ValueError:
        print ("Tienes que ingresar un año no caracteres")