#Sesion 7
#Ciclo for

guias = ["G001", "G002", "G003", "G004", "G005"]

for guia in guias:
    print("Revisando envío:", guia)

#for + range

for consecutivo in range (2):
    print("revisando envío:", guias [consecutivo])

for consecutivo in range (2, 5):
    print("revisando envío:", guias [consecutivo])

#contadores

contador = 0

for guia in guias:
    contador += 1
    print ("revisando guias:", guia)

print ("Total contador:", contador)

#Acumulador de KM

distancias = [15, 22, 10, 18]

distancia_total = 0

for distancia in distancias:
    distancia_total += distancia

print ("Distancia total:", distancia_total)

#ciclo while
#intentos de entrega

envios = [
    {"estado": "Entregado"},
    {"estado": "En ruta"},
    {"estado": "Devuelto"},
    {"estado": "Entregado"},
    {"estado": "Devuelto"},
    {"estado": "Entregado"},
]

entregados = 0
en_ruta = 0
devueltos = 0

for envio in envios:

    if envio["estado"] == "Entregado":
        entregados += 1

    elif envio["estado"] == "En ruta":
        en_ruta += 1

    else:
        devueltos +=1

#mostrar resultados

print("RESUMEN DE ENVIOS")
print("Entregados", entregados)
print("En ruta", en_ruta)
print("Devueltos", devueltos)

#while #
#intentos de entrega

guia = "G001"

intentos = 0
entregados = False

while intentos < 3 and entregados == False:
    intentos +=1

print("guia", guia)  
print("intentos de entrega", intentos)

resultado = input("se entrego el paquete (s/n):  ").lower()

if resultado =="s":
    entregados = True
else:
    entregados = False

if entregados:
    print("Envío entregado")
else:
    print("Envío devuelto")

#Frecuencias de entregas en tiempo

tiempos = [1,2,3,4,5,6,7,8,9,10,11,12]

grupo_1_3 = 0
grupo_4_6 = 0
grupo_7_9 = 0
grupo_10_12 = 0

for tiempo in tiempos:
    if 1<= tiempo <=3:
        grupo_1_3 +=1
    elif 4 <= tiempo <=6:
        grupo_4_6 +=1
    elif 7 <= tiempo <=9:
        grupo_7_9 +=1
    elif 10 <= tiempo <=12:
        grupo_10_12 +=1

print("REPORTE DE TIEMPOS DE ENTREGA")
print("de 1 a 3 días", grupo_1_3, "entregas")
print("de 1 a 3 días", grupo_4_6, "entregas")
print("de 1 a 3 días", grupo_7_9, "entregas")
print("de 1 a 3 días", grupo_10_12, "entregas")