# ==========================================================
# RETO INTEGRADOR - SESION 6
# PRIORIZADOR DE SOLICITUDES ADMINISTRATIVAS
# ==========================================================

# 1. Crear el diccionario con los datos de entrada
solicitud = {
    "codigo": "ADM-004",
    "tipo": "Actualizacion de datos",
    "area_solicitante": "Talento Humano",
    "dias_pendiente": 3,
    "afecta_operacion": True,
    "estado": "Pendiente"
}

# 2, 3 y 4. Evaluar las reglas en el orden indicado
# y asignar la clasificacion y la accion

if solicitud["estado"] == "Cerrada":
    clasificacion = "CERRADA"
    accion = "Registrar que no requiere nueva gestion"

elif solicitud["afecta_operacion"] and solicitud["dias_pendiente"] >= 2:
    clasificacion = "URGENTE"
    accion = "Escalar al responsable para atencion prioritaria"

elif solicitud["afecta_operacion"] or solicitud["dias_pendiente"] >= 5:
    clasificacion = "PRIORITARIA"
    accion = "Programar atencion preferente"

else:
    clasificacion = "NORMAL"
    accion = "Mantener en el flujo habitual de atencion"

# 5. Mostrar el resumen usando una f-string
print(
    f"Codigo: {solicitud['codigo']} | "
    f"Tipo: {solicitud['tipo']} | "
    f"Clasificacion: {clasificacion} | "
    f"Accion recomendada: {accion}"
)