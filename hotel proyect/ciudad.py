# ============================================================
# ciudad.py — Definición de ciudades y sus hoteles
# Cada ciudad tiene instancias propias e independientes
# de hoteles para que la capacidad no se comparta entre ellas
# ============================================================

from hotel import Hotel

class Ciudad:
  def __init__(self, nombreciudad):
    self.nombreciudad = nombreciudad
    self.hoteles = []

  def agregar_hotel(self, hotel):
    self.hoteles.append(hotel)

def crear_hoteles():
  return [
    Hotel("El Paraiso",       4, 3),
    Hotel("Descansar",        3, 2),
    Hotel("Caribbean Resort", 5, 5),
  ]

c1 = Ciudad("Barranquilla")
c2 = Ciudad("Bogotá")
c3 = Ciudad("Medellin")

for ciudad in [c1, c2, c3]:
  for hotel in crear_hoteles():
    ciudad.agregar_hotel(hotel)

ciudades = [c1, c2, c3]
