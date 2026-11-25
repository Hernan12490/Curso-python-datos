# ==================================================
# 1. DICCIONARIO DE DATOS
# ==================================================

flota = [
    {"codigo": "V-101", "km": 320},
    {"codigo": "V-102", "km": 780},
    {"codigo": "V-103", "km": 1250},
    {"codigo": "V-104", "km": 1680},
    {"codigo": "V-105", "km": 450},
    {"codigo": "V-106", "km": 920},
    {"codigo": "V-107", "km": 1420},
    {"codigo": "V-108", "km": 1850},
    {"codigo": "V-109", "km": 610},
    {"codigo": "V-110", "km": 1100},
    {"codigo": "V-111", "km": 250},
    {"codigo": "V-112", "km": 1550}
]


# ==================================================
# 2. CONTADORES Y ACUMULADOR
# ==================================================

uso_reciente = 0
seguimiento = 0
programar_revision = 0
prioridad_alta = 0

total_km = 0


# ==================================================
# 3. RECORRER Y CLASIFICAR LOS VEHICULOS
# ==================================================

for vehiculo in flota:

    codigo = vehiculo["codigo"]
    km = vehiculo["km"]

    total_km = total_km + km

    if km <= 499:
        categoria = "Uso reciente"
        uso_reciente = uso_reciente + 1

    elif km <= 999:
        categoria = "Seguimiento"
        seguimiento = seguimiento + 1

    elif km <= 1499:
        categoria = "Programar revision"
        programar_revision = programar_revision + 1

    else:
        categoria = "Prioridad alta"
        prioridad_alta = prioridad_alta + 1

    print(codigo, "-", km, "km -", categoria)


# ==================================================
# 4. MOSTRAR RESUMEN
# ==================================================

print()
print("RESUMEN DE LA FLOTA")
print("Uso reciente:", uso_reciente)
print("Seguimiento:", seguimiento)
print("Programar revision:", programar_revision)
print("Prioridad alta:", prioridad_alta)

print()
print("Kilometraje total:", total_km, "km")


# ==================================================
# 5. CALCULAR PROMEDIO
# ==================================================

promedio_km = total_km / len(flota)

print("Kilometraje promedio:", promedio_km, "km")


# ==================================================
# 6. CONSULTAR VEHICULO
# ==================================================

print()

continuar = "si"

while continuar == "si":

    codigo_buscar = input("Ingrese el codigo del vehiculo: ")

    encontrado = False

    for vehiculo in flota:

        if vehiculo["codigo"] == codigo_buscar:

            km = vehiculo["km"]

            if km <= 499:
                categoria = "Uso reciente"

            elif km <= 999:
                categoria = "Seguimiento"

            elif km <= 1499:
                categoria = "Programar revision"

            else:
                categoria = "Prioridad alta"

            print("Vehiculo:", vehiculo["codigo"])
            print("Kilometraje:", km, "km")
            print("Categoria:", categoria)

            encontrado = True

    if encontrado == False:
        print("Vehiculo no encontrado")

    continuar = input("Desea realizar otra consulta? si/no: ")

    # ==================================================
# 7. RESPUESTAS A LAS PREGUNTAS
# ==================================================

# 1. ¿En que intervalo esta la mayor cantidad de vehiculos?
# En este caso no existe un solo intervalo con mayor cantidad,
# porque las cuatro categorias tienen 3 vehiculos cada una.
# Por lo tanto, todas tienen la misma frecuencia.

# 2. ¿Cuantos vehiculos estan en Programar revision y Prioridad alta?
# En Programar revision hay 3 vehiculos y en Prioridad alta hay 3.
# En total, 6 vehiculos requieren programar revision o tienen
# prioridad alta.

# 3. ¿Que representa el kilometraje promedio?
# El kilometraje promedio representa la cantidad media de kilometros
# recorridos por los vehiculos desde su ultimo mantenimiento.
# En este caso el promedio es de 1015 km.

# 4. ¿Por que el promedio no permite saber por si solo cuales
# vehiculos requieren atencion?
# Porque el promedio presenta un valor general de toda la flota,
# pero cada vehiculo tiene un kilometraje diferente.
# Por ejemplo, V-111 tiene 250 km y se encuentra en Uso reciente,
# mientras que V-108 tiene 1850 km y se encuentra en Prioridad alta.
# Por eso es necesario revisar y clasificar cada vehiculo.