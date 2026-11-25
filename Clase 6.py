#Sesion 6
#if

cantidad_productos = 3
if cantidad_productos <= 3:
    print("bajo stock")

#Prueba 1

saldo_factura = 850000

if saldo_factura > 0:
    print("La factura tiene saldo pendiente de pago")

#Prueba 2

saldo_factura = 150000

if saldo_factura > 0:
    print("La factura tiene saldo pendiente de pago")

#Prueba 3

saldo_factura = 0

if saldo_factura > 0:
    print("La factura tiene saldo pendiente de pago")

#if else

total_compra = 300000
if total_compra >= 100000:
    print("descuento autorizado")
else:
    print("no aplica descuento")

#Actividad

saldo_factura = 850000

if saldo_factura > 0:
    print("La factura requiere gestion de cobro")
else:
    print("La factura no tiene saldo pendiente")

#tabla de pruebas

cantidad = 8

if cantidad == 0:
    print("Agotado")
elif cantidad <= 5:
    print("Inventario bajo")
else:
    print("Disponible")


#Ejercicio

saldo_factura = 850000
factura_vencida = True

if saldo_factura > 0 and factura_vencida:
    print("Factura prioritaria para gestion de cobro")
else:
    print("Factura sin prioridad de cobro")

#reto

factura = {
    "numero": "F001",
    "valor": 850000,
    "dias_pendiente": 25,
    "tiene_soportes": True
}

if factura["dias_pendiente"] > 20 and factura["tiene_soportes"]:
    print("Prioridad: URGENTE")
    print("Accion: radicar la factura inmediatamente")

elif factura["dias_pendiente"] > 10:
    print("Prioridad: PRIORITARIA")
    print("Accion: revisar la factura para radicacion")

else:
    print("Prioridad: NORMAL")
    print("Accion: continuar el proceso habitual")