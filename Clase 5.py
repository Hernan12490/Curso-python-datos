#Sesion 5

#Diccionarios

televisores = {
    "marca": "Samsung",
     "precio": 5400000,
      "pulgadas": 50,
       "color": "negro",
        "resolucion":"4k",
}

print (televisores ["marca"])
print (televisores ["precio"])
print (televisores ["pulgadas"])
print (televisores ["color"])
print (televisores ["resolucion"])

#Consulta información get
#Corchetes [] mala consulta

print (televisores ["precio"])

#parentesis - buena consulta

print (televisores.get ("disponible"))
print (televisores.get ("precio"))
print (televisores.get ("pulgadas"))

#Agregar información

televisores["disponible"] = False
print (televisores)

#modificar información

televisores["precio"] = 6000000
print (televisores)

#Eliminar información

del televisores ["disponible"]
print (televisores)

#Consultar grupos de datos

print (televisores.keys())
print (televisores.values())
print (televisores.items())

#Colección de registros

electrodomesticos_cocina = [
    {
        "producto": "microondas",
         "marca": "LG",
          "litros": 22,
           "color": "plateado",
            "disponible": True,
    },
    {
         "producto": "sanduchera",
         "marca": "oster",
          "color": "negro",
          "disponible": True,

    }
]

print(electrodomesticos_cocina[0]["marca"])
print(electrodomesticos_cocina[1]["marca"])

#ejemplo vs CODE

producto_1 = {"codigo": "HV1", "nombre": "consulta", "precio":25000}
producto_2 = {"codigo": "HV2", "nombre": "laboratorio", "precio":35000}

inventario = [producto_1, producto_2]

print("primer producto:", inventario[0]["nombre"])
print("precio del segundo:", inventario[1]["precio"])

inventario[0]["precio"] = 15000
print("nuevo precio:", inventario[0]["precio"])

#conjuntos

canales = {"Instagram", "Facebook", "Tiktok"}

print(canales)

#agregar un canal
canales.add("Linkedin")

print(canales)

#Comprobar si un elemento está en un conjunto

print("Instagram" in canales)
print("YouTube" in canales)

#unir dos conjuntos

campania_a = {"Instagram", "Facebook", "Tiktok"}
campania_b = {"Linkedin", "YouTube", "Tiktok"}
campania_C = campania_a | campania_b

print(campania_C)

campania_d = campania_a & campania_b

print(campania_d)

campania_e = campania_a - campania_b

print(campania_e)