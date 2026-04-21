# ============================================================
# hotel.py — Definición de hoteles y asignación de planes
# Los planes se asignan automáticamente según las estrellas
# del hotel usando el mapa PLANES_POR_ESTRELLAS de plan.py
# ============================================================

from plan import PLANES_POR_ESTRELLAS

class Hotel:
  def __init__(self, nombrehotel, estrellas, capacidad):
    self.nombrehotel       = nombrehotel
    self.estrellas         = estrellas
    self.capacidad         = capacidad
    self.huespedes_actuales = 0
    self.reservas          = []
    # Asignar planes automáticamente según calidad del hotel
    self.planes = list(PLANES_POR_ESTRELLAS.get(estrellas, []))

  def agregar_plan(self, plan):
    self.planes.append(plan)

  def hay_capacidad(self):
    return self.huespedes_actuales < self.capacidad

  def ocupar(self, cantidad):
    self.huespedes_actuales += cantidad

  def liberar(self, cantidad):
    self.huespedes_actuales -= cantidad
