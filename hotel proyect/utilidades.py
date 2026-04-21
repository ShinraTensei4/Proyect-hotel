# ============================================================
# utilidades.py — Funciones auxiliares reutilizables
# Separadas para evitar imports circulares entre módulos
# ============================================================

# --- Validación estricta de respuestas s/n ---
def preguntar_si_no(mensaje):
  while True:
    respuesta = input(mensaje).strip().lower()
    if respuesta == "s":
      return True
    elif respuesta == "n":
      return False
    else:
      print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
