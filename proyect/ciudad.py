from hotel import Hotel, h1, h2, h3

class Ciudad:
  def __init__(self, nombreciudad):
    self.nombreciudad = nombreciudad
    self.hoteles = []

  def agregar_hotel(self, hotel):
    self.hoteles.append(hotel)

ciudades = []

c1=Ciudad("Barranquilla")
c2=Ciudad("Bogotá")
c3=Ciudad("Medellin")

ciudades.append(c1)
ciudades.append(c2)
ciudades.append(c3)


from plan import p1, p2, p3, p4

def crear_hoteles_ciudad():
  ha1=Hotel("El paraiso", 4, 3)
  ha2=Hotel("Descansar", 3, 2)
  ha3=Hotel("Caribbean Resort", 5, 5)
  for h in [ha1, ha2, ha3]:
    h.agregar_plan(p1)
    h.agregar_plan(p2)
    h.agregar_plan(p3)
    h.agregar_plan(p4)
  return ha1, ha2, ha3

bq1, bq2, bq3 = crear_hoteles_ciudad()
bog1, bog2, bog3 = crear_hoteles_ciudad()
med1, med2, med3 = crear_hoteles_ciudad()

c1.agregar_hotel(bq1)
c1.agregar_hotel(bq2)
c1.agregar_hotel(bq3)

c2.agregar_hotel(bog1)
c2.agregar_hotel(bog2)
c2.agregar_hotel(bog3)

c3.agregar_hotel(med1)
c3.agregar_hotel(med2)
c3.agregar_hotel(med3)
