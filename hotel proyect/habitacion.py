# ============================================================
# habitacion.py — Definición de habitaciones por calidad
# Cada nivel de estrellas tiene sus propias habitaciones
# con costos noche y costo adicional de minibar diferenciados
# ============================================================

class Habitacion:
  def __init__(self, calidad, capacidad, costonoche, costo_minibar=0):
    self.calidad      = calidad
    self.capacidad    = capacidad
    self.costonoche   = costonoche
    self.costo_minibar = costo_minibar  # 0 = sin minibar disponible

  @property
  def minibar(self):
    return self.costo_minibar > 0

# --- Habitaciones para hoteles de 3 estrellas ---
h3_basica   = Habitacion("Basica",   2, 40000,  costo_minibar=0)
h3_estandar = Habitacion("Estandar", 3, 70000,  costo_minibar=0)
h3_premium  = Habitacion("Premium",  4, 100000, costo_minibar=15000)
h3_deluxe   = Habitacion("Deluxe",   6, 140000, costo_minibar=20000)

# --- Habitaciones para hoteles de 4 estrellas ---
h4_basica   = Habitacion("Basica",   2, 60000,  costo_minibar=0)
h4_estandar = Habitacion("Estandar", 3, 95000,  costo_minibar=0)
h4_premium  = Habitacion("Premium",  4, 130000, costo_minibar=20000)
h4_deluxe   = Habitacion("Deluxe",   8, 180000, costo_minibar=30000)

# --- Habitaciones para hoteles de 5 estrellas ---
h5_basica   = Habitacion("Basica",   2, 90000,  costo_minibar=0)
h5_estandar = Habitacion("Estandar", 3, 140000, costo_minibar=0)
h5_premium  = Habitacion("Premium",  4, 200000, costo_minibar=35000)
h5_deluxe   = Habitacion("Deluxe",   8, 280000, costo_minibar=50000)
