from plan import p1, p2, p3, p4

class Hotel:
  def __init__(self, nombrehotel, estrellas, capacidad):
    self.nombrehotel = nombrehotel
    self.estrellas = estrellas
    self.capacidad = capacidad
    self.huespedes_actuales = 0
    self.planes = []
    self.reservas = []

  def agregar_plan(self, plan):
    self.planes.append(plan)

  def hay_capacidad(self):
    return self.huespedes_actuales < self.capacidad

  def ocupar(self, cantidad):
    self.huespedes_actuales += cantidad

  def liberar(self, cantidad):
    self.huespedes_actuales -= cantidad

h1=Hotel("El paraiso", 4, 3)
h2=Hotel("Descansar", 3, 2)
h3=Hotel("Caribbean Resort", 5, 5)

h1.agregar_plan(p1)
h1.agregar_plan(p2)
h1.agregar_plan(p3)
h1.agregar_plan(p4)

h2.agregar_plan(p1)
h2.agregar_plan(p2)
h2.agregar_plan(p3)
h2.agregar_plan(p4)

h3.agregar_plan(p1)
h3.agregar_plan(p2)
h3.agregar_plan(p3)
h3.agregar_plan(p4)
