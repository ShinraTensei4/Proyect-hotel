from habitacion import hbasica, hestandar, hpremium, hdeluxe

class Plan:
  def __init__(self, nombreplan, habitacion):
    self.nombreplan = nombreplan
    self.habitacion = habitacion

  def costo_total(self, noches):
    return self.habitacion.costonoche * noches

p1=Plan("Basic", hbasica)
p2=Plan("Mid", hestandar)
p3=Plan("High", hpremium)
p4=Plan("Deluxe", hdeluxe)
