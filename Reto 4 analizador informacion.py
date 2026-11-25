# RETO INTEGRADOR
# Mi primer analizador de informacion

# Cadena
area = "Facturacion hospitalaria"

# Tupla con las sedes
sedes = ("Bogota", "Medellin", "Cali")

# Lista con dias ficticios de radicacion
dias_radicacion = [8, 12, 10, 8, 15, 9, 8, 14]

# Media
total = sum(dias_radicacion)
media = total / len(dias_radicacion)

# Ordenar los datos
ordenados = sorted(dias_radicacion)

# Mediana
mediana = (ordenados[3] + ordenados[4]) / 2

# Moda
moda = max(dias_radicacion, key=dias_radicacion.count)

# Frecuencia
frecuencia_8 = dias_radicacion.count(8)

# Mostrar resultados
print("== ANALISIS DE RADICACION DE FACTURAS ===")
print("Area:", area)

print("\nSEDES")
print("Sedes analizadas:", sedes)

print("\nDATOS")
print("Dias de radicacion:", dias_radicacion)
print("Datos ordenados:", ordenados)

print("\nRESULTADOS ESTADISTICOS")
print("Media:", media, "dias")
print("Mediana:", mediana, "dias")
print("Moda:", moda, "dias")
print("Frecuencia del valor 8:", frecuencia_8)