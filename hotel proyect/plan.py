# ============================================================
# plan.py — Definición de planes por calidad de hotel
# Cada plan vincula una habitación y permite incluir minibar
# como costo adicional opcional al momento de la reserva
# ============================================================

from habitacion import (
  h3_basica, h3_estandar, h3_premium, h3_deluxe,
  h4_basica, h4_estandar, h4_premium, h4_deluxe,
  h5_basica, h5_estandar, h5_premium, h5_deluxe
)

class Plan:
  def __init__(self, nombreplan, habitacion):
    self.nombreplan = nombreplan
    self.habitacion = habitacion

  # Costo base sin minibar
  def costo_total(self, noches, con_minibar=False):
    base = self.habitacion.costonoche * noches
    extra = self.habitacion.costo_minibar * noches if con_minibar else 0
    return base + extra

# --- Planes para hoteles de 3 estrellas ---
p3_basica   = Plan("Basic",  h3_basica)
p3_estandar = Plan("Mid",    h3_estandar)
p3_premium  = Plan("High",   h3_premium)
p3_deluxe   = Plan("Deluxe", h3_deluxe)

# --- Planes para hoteles de 4 estrellas ---
p4_basica   = Plan("Basic",  h4_basica)
p4_estandar = Plan("Mid",    h4_estandar)
p4_premium  = Plan("High",   h4_premium)
p4_deluxe   = Plan("Deluxe", h4_deluxe)

# --- Planes para hoteles de 5 estrellas ---
p5_basica   = Plan("Basic",  h5_basica)
p5_estandar = Plan("Mid",    h5_estandar)
p5_premium  = Plan("High",   h5_premium)
p5_deluxe   = Plan("Deluxe", h5_deluxe)

# Mapa de estrellas → lista de planes del hotel
PLANES_POR_ESTRELLAS = {
  3: [p3_basica, p3_estandar, p3_premium, p3_deluxe],
  4: [p4_basica, p4_estandar, p4_premium, p4_deluxe],
  5: [p5_basica, p5_estandar, p5_premium, p5_deluxe],
}
