from datetime import datetime, timedelta
from clientes import Cliente, clientes
from ciudad import ciudades
from reserva import Reserva
from plan import Plan

def preguntar_si_no(mensaje):
  while True:
    respuesta = input(mensaje).strip().lower()
    if respuesta == "s":
      return True
    elif respuesta == "n":
      return False
    else:
      print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")

def registrar_cliente():
  print("BIENVENIDO AL SISTEMA")
  while True:
    nombrecliente = input("Ingrese su nombre: ").strip()
    if nombrecliente == "":
      print("El nombre no puede estar vacío.")
    elif not nombrecliente.replace(" ", "").isalpha():
      print("El nombre NO puede contener números.")
    else:
      break

  while True:
    dni = input("Ingrese su DNI: ").strip()
    if dni == "":
      print("El DNI no puede estar vacío.")
    elif not dni.isdigit():
      print("El DNI NO puede contener letras.")
    elif len(dni) < 6:
      print("El DNI es muy corto.")
    elif len(dni) > 10:
      print("El DNI es invalido.")
    else:
      break

  
  for c in clientes:
    if c.dni == dni:
      if c.nombrecliente.lower() == nombrecliente.lower():
        print(f"\nCliente reconocido. Bienvenido de nuevo, {c.nombrecliente}!")
        return c, True
      else:
        print("Ya existe un cliente con ese DNI pero diferente nombre. Verifique sus datos.")
        return registrar_cliente()

  
  for c in clientes:
    if c.nombrecliente.lower() == nombrecliente.lower() and c.dni != dni:
      print("Ya existe un cliente con ese nombre pero diferente DNI. Use otro nombre o verifique su DNI.")
      return registrar_cliente()

  cliente = Cliente(nombrecliente, dni)
  clientes.append(cliente)
  return cliente, False

def menu_cliente_recurrente(cliente):
  while True:
    print(f"\n--- MENÚ DE {cliente.nombrecliente.upper()} ---")
    print("1. Ver mis reservas")
    print("2. Realizar una nueva reserva")
    print("3. Cerrar sesión")
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
      if not cliente.reservas:
        print("No tiene reservas registradas aún.")
      else:
        print(f"\n--- RESERVAS DE {cliente.nombrecliente} ---")
        for i, r in enumerate(cliente.reservas, start=1):
          print(f"\nReserva #{i}")
          r.mostrar()
    elif opcion == "2":
      return True
    elif opcion == "3":
      return False
    else:
      print("Opción inválida.")

def seleccionar_ciudad(ciudades):
  while True:
    print("\n--- CIUDADES DISPONIBLES ---")
    for i, ciudad in enumerate(ciudades, start=1):
      print(f"{i}. {ciudad.nombreciudad}")
    opcion = input("Elige una ciudad: ")
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(ciudades):
        return ciudades[opcion - 1]
      else:
        print("Número fuera de rango")
    else:
      print("Opción inválida")

def seleccionar_hotel(ciudad):
  while True:
    print(f"\n--- HOTELES EN {ciudad.nombreciudad} ---")
    for i, hotel in enumerate(ciudad.hoteles, start=1):
      disponibles = hotel.capacidad - hotel.huespedes_actuales
      print(f"{i}. {hotel.nombrehotel} - {hotel.estrellas} estrellas | Cupos disponibles: {disponibles}/{hotel.capacidad}")
    opcion = input("Elige un hotel: ")
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(ciudad.hoteles):
        hotel = ciudad.hoteles[opcion - 1]
        if not hotel.hay_capacidad():
          print(f"Lo sentimos, el hotel {hotel.nombrehotel} no tiene capacidad disponible.")
        else:
          return hotel
      else:
        print("Número fuera de rango")
    else:
      print("Opción inválida")

def seleccionar_fechas(cliente, hotel):
  while True:
    print("\n--- SELECCIÓN DE FECHAS ---")
    while True:
      fecha_entrada_str = input("Ingrese fecha de check-in (DD/MM/AAAA): ").strip()
      try:
        fecha_entrada = datetime.strptime(fecha_entrada_str, "%d/%m/%Y")
        if fecha_entrada < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
          print("La fecha de check-in no puede ser en el pasado.")
        else:
          break
      except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")

    while True:
      fecha_salida_str = input("Ingrese fecha de check-out (DD/MM/AAAA): ").strip()
      try:
        fecha_salida = datetime.strptime(fecha_salida_str, "%d/%m/%Y")
        if fecha_salida <= fecha_entrada:
          print("La fecha de check-out debe ser posterior al check-in.")
        else:
          break
      except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")

    noches = (fecha_salida - fecha_entrada).days

    conflicto = False
    for r in cliente.reservas:
      if r.hotel is hotel and r.fechas_se_interceptan(fecha_entrada, fecha_salida):
        print(f"Ya tiene una reserva en este hotel del {r.fecha_entrada.strftime('%d/%m/%Y')} al {r.fecha_salida.strftime('%d/%m/%Y')}.")
        print("Las fechas se interceptan. Elija otras fechas.")
        conflicto = True
        break

    if not conflicto:
      return fecha_entrada, fecha_salida, noches

def seleccionar_plan(hotel, noches):
  while True:
    print("\n--- PLANES DISPONIBLES ---")
    for i, plan in enumerate(hotel.planes, start=1):
      minibar = " | Incluye minibar" if plan.habitacion.minibar else ""
      total = plan.costo_total(noches)
      print(f"{i}. Plan {plan.nombreplan} | Hab. {plan.habitacion.calidad} | "
            f"Cap. {plan.habitacion.capacidad} personas | "
            f"${plan.habitacion.costonoche:,.0f}/noche | "
            f"Total {noches} noches: ${total:,.0f}{minibar}")
    opcion = input("Elige un plan: ")
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(hotel.planes):
        return hotel.planes[opcion - 1]
      else:
        print("Número fuera de rango")
    else:
      print("Opción inválida")

def flujo_reserva(cliente):
  ciudad = seleccionar_ciudad(ciudades)
  hotel = seleccionar_hotel(ciudad)
  fecha_entrada, fecha_salida, noches = seleccionar_fechas(cliente, hotel)
  plan = seleccionar_plan(hotel, noches)
  costototal = plan.costo_total(noches)

  reserva = Reserva(cliente, ciudad, hotel, plan, fecha_entrada, fecha_salida, noches, costototal)
  cliente.reservas.append(reserva)
  hotel.ocupar(1)

  print("\n--- RESERVA CONFIRMADA ---")
  reserva.mostrar()

def main():
  while True:
    resultado = registrar_cliente()
    cliente, es_recurrente = resultado

    if es_recurrente:
      while True:
        hacer_reserva = menu_cliente_recurrente(cliente)
        if hacer_reserva:
          flujo_reserva(cliente)
          if not preguntar_si_no("\n¿Desea realizar otra reserva? (s/n): "):
            break
        else:
          break
    else:
      flujo_reserva(cliente)
      while preguntar_si_no("\n¿Desea realizar otra reserva? (s/n): "):
        flujo_reserva(cliente)

    if not preguntar_si_no("\n¿Desea registrar otro cliente? (s/n): "):
      print("Gracias por usar el sistema. ¡Hasta pronto!")
      break

main()
