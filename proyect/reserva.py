class Reserva:
  def __init__(self, cliente, ciudad, hotel, plan, fecha_entrada, fecha_salida, noches, costototal):
    self.cliente = cliente
    self.ciudad = ciudad
    self.hotel = hotel
    self.plan = plan
    self.fecha_entrada = fecha_entrada
    self.fecha_salida = fecha_salida
    self.noches = noches
    self.costototal = costototal

  def fechas_se_interceptan(self, fecha_entrada, fecha_salida):
    return not (fecha_salida <= self.fecha_entrada or fecha_entrada >= self.fecha_salida)

  def mostrar(self):
    minibar = "Sí" if self.plan.habitacion.minibar else "No"
    print("=" * 40)
    print(f"  RESERVA - {self.hotel.nombrehotel}")
    print("=" * 40)
    print(f"  Cliente       : {self.cliente.nombrecliente}")
    print(f"  DNI           : {self.cliente.dni}")
    print(f"  Ciudad        : {self.ciudad.nombreciudad}")
    print(f"  Hotel         : {self.hotel.nombrehotel} ({self.hotel.estrellas} estrellas)")
    print(f"  Plan          : {self.plan.nombreplan}")
    print(f"  Habitación    : {self.plan.habitacion.calidad}")
    print(f"  Minibar       : {minibar}")
    print(f"  Check-in      : {self.fecha_entrada.strftime('%d/%m/%Y')}")
    print(f"  Check-out     : {self.fecha_salida.strftime('%d/%m/%Y')}")
    print(f"  Noches        : {self.noches}")
    print(f"  Valor/noche   : ${self.plan.habitacion.costonoche:,.0f}")
    print(f"  TOTAL         : ${self.costototal:,.0f}")
    print("=" * 40)
