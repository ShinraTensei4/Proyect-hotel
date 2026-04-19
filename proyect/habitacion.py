class Habitacion:
  def __init__(self, calidad, capacidad, costonoche, minibar=False):
    self.calidad = calidad
    self.capacidad = capacidad
    self.costonoche = costonoche
    self.minibar = minibar

hbasica=Habitacion("Basica", 2, 30000)
hestandar=Habitacion("Estandar", 3, 60000)
hpremium=Habitacion("Premium", 4, 85000, minibar=True)
hdeluxe=Habitacion("Deluxe", 8, 120000, minibar=True)
