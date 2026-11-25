#SESION 4
#CONSULTAR CADENAS TEXTO

Producto="monitor"
print (Producto [0]) # m
print (Producto [1]) # o
print (Producto [2]) # n
print (Producto [3]) # i
print (Producto [4]) # t
print (Producto [5]) # o
print (Producto [6]) # r

#f string construir mensajes con variables

print (f"el producto es: {Producto}")

#Posiciones positivas y negativas

print(Producto[6])
print(Producto[-1])
print(Producto[0])

#Extraer partes de una cadena de texto

print(Producto[0:3]) # mon
print(Producto[2:5]) # nit
print(Producto[2:]) # nitor
print(Producto[:-3]) # moni
print(Producto[2:-3]) # ni

#Longitud de una cadena de texto incluyendo espacios

Producto="memoria RAM 16 gb"
longitud = (len(Producto))
print("la longitud de la cadena de texto es:",longitud)

#metodos de cadenas de texto
#convertir a mayusculas

Producto="memoria ram 16 gb"
print(Producto.upper())

#convertir a minuscula

print(Producto.lower())

#capitalizar la primera letra de una cadena de texto

print(Producto.capitalize())

#reemplazar un caracter

print(Producto.replace("a","e"))

#agregar una letra al final de cada cadena de texto

print(Producto + " s ")

#eliminar espacios en blanco al inicio y al final de la cadena de texto

print(Producto.strip())

#limpiar base de datos

nombre = "   JUAN CARLOS LOPEZ GONZALEZ   "
print(f"El nombre del cliente es: {nombre.strip().title()}")

#practica

Nombres = [ " MARIA GOMEZ ",
           "juan perez",
           " ANA LOPEZ "]

#consulta el primer nombre

print(Nombres[0])

#limpia el primer nombre

Nombres[0] = Nombres[0].strip()

print(Nombres[0])

# convertir formato a titulo

Nombres[0] = Nombres[0].title()

print(Nombres[0])

#listas

lista = ["monitor",
         "teclado",
         "mouse",
         "pendrive"]

print(lista)

#agregar un elemento al final de la lista

lista.append("impresora")
print(lista)

#agregar un elemento en una posición específica

lista.insert(1, "dico duro")
print(lista)

#eliminar un elemento de la lista

lista.remove("pendrive")
print(lista)

#eliminar un elemento de la lista por su posicion

del lista [2]
print(lista)

#ordenar una lista

lista.sort()
print(lista)

#ordenar una lista inversa

lista.sort(reverse=True)
print(lista)

#unir dos listas

lista2 = ["teclado inalambrico", "mouse inalambrico", "pendrive externo"]
lista3 =  lista + lista2
print(lista3)

#convertir una cadena de texto en una lista

cadena = "monitor, teclado, mouse, pendrive"
lista4 = cadena.split(",")
print(lista4)

#contar la cantidad elementos de una lista

print(len(lista4))

#ejercicio

#crear una lista

ventas = [12, 18, 15, 20, 10]
print("Lista inicial:", ventas)

#consultar un elemento

print("Ventas del segundo día:", ventas[1])

#modificar un elemento

#agregar un elemento

ventas.append("25")
print(ventas)

#agregar un elemento en una posición específica

lista.insert(1, "dico duro")
print(lista)

#eliminar un elemento de la lista

lista.remove("pendrive")
print(lista)