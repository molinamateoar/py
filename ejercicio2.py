producto=input("Ingrese producto:")

try: 
    precio=float(input("Ingrese precio del producto:"))
    cantidad=int(input("Ingrese cantidad de unidades:"))
    total=cantidad*precio
    if 5000<total:
         total=total-(total*0.10)
        
    print (f"Producto {producto}")
    print (f"Precio:$ {precio}")
    print (f"Cantidad:{cantidad}")
    print (f"Total:{total}")
except ValueError:
    print ("Debe ingresar una cantidad entera o numero decimal con puntos")


   