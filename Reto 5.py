# RETO INTEGRADOR 1 - MI INVENTARIO


# ENTRADA

producto_1 = {
    "codigo": "HV1",
    "nombre": "consulta",
    "precio": 25000,
    "cantidad": 10,
    "categoria": "Consulta"
}

producto_2 = {
    "codigo": "HV2",
    "nombre": "laboratorio",
    "precio": 35000,
    "cantidad": 5,
    "categoria": "Laboratorio"
}

producto_3 = {
    "codigo": "HV3",
    "nombre": "hemograma",
    "precio": 20000,
    "cantidad": 8,
    "categoria": "Laboratorio"
}


# PROCESO

# Guardar los productos en una lista
inventario = [producto_1, producto_2, producto_3]

# Consultar el nombre de un producto
print("Primer producto:", inventario[0].get("nombre"))

# Modificar el precio de un producto
inventario[0]["precio"] = 30000

# Modificar la cantidad de un producto
inventario[1]["cantidad"] = 7

# Crear un conjunto de categorias
categorias = {
    producto_1["categoria"],
    producto_2["categoria"],
    producto_3["categoria"]
}


# SALIDA

print("Nuevo precio:", inventario[0]["precio"])
print("Nueva cantidad:", inventario[1]["cantidad"])
print("Categorias unicas:", categorias)
print("Inventario:", inventario)