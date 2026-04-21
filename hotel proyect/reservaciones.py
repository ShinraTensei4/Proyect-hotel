# ============================================================
# reservaciones.py — Lógica de selección y flujo de reserva
# Contiene todas las funciones de interacción relacionadas
# con ciudades, hoteles, fechas, planes y confirmación
# Importado por main_1.py para mantenerlo limpio y ordenado
# ============================================================

from datetime import datetime
from ciudad import ciudades
from reserva import Reserva

# --- Selección de ciudad ---
def seleccionar_ciudad():
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
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

# --- Selección de hotel dentro de una ciudad ---
def seleccionar_hotel(ciudad):
  while True:
    print(f"\n--- HOTELES EN {ciudad.nombreciudad} ---")
    for i, hotel in enumerate(ciudad.hoteles, start=1):
      disponibles = hotel.capacidad - hotel.huespedes_actuales
      print(f"{i}. {hotel.nombrehotel} — {hotel.estrellas} estrellas | "
            f"Cupos disponibles: {disponibles}/{hotel.capacidad}")
    opcion = input("Elige un hotel: ")
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(ciudad.hoteles):
        hotel = ciudad.hoteles[opcion - 1]
        if not hotel.hay_capacidad():
          print(f"Lo sentimos, '{hotel.nombrehotel}' no tiene capacidad disponible.")
        else:
          return hotel
      else:
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

# --- Ingreso y validación de fechas de hospedaje ---
def seleccionar_fechas(cliente, hotel):
  while True:
    print("\n--- SELECCIÓN DE FECHAS ---")

    # Ingreso fecha check-in
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

    # Ingreso fecha check-out
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

    # Verificación de fechas solapadas con reservas existentes
    conflicto = False
    for r in cliente.reservas:
      if r.hotel is hotel and r.fechas_se_interceptan(fecha_entrada, fecha_salida):
        print(f"Ya tiene una reserva en este hotel del "
              f"{r.fecha_entrada.strftime('%d/%m/%Y')} al {r.fecha_salida.strftime('%d/%m/%Y')}.")
        print("Las fechas se interceptan. Elija otras fechas.")
        conflicto = True
        break

    if not conflicto:
      return fecha_entrada, fecha_salida, noches

# --- Selección de plan y opción de minibar ---
def seleccionar_plan(hotel, noches):
  while True:
    print("\n--- PLANES DISPONIBLES ---")
    for i, plan in enumerate(hotel.planes, start=1):
      base = plan.costo_total(noches, con_minibar=False)
      if plan.habitacion.minibar:
        con_mb = plan.costo_total(noches, con_minibar=True)
        minibar_txt = (f" | Minibar disponible: +${plan.habitacion.costo_minibar:,.0f}/noche "
                       f"(total con minibar: ${con_mb:,.0f})")
      else:
        minibar_txt = ""
      print(f"{i}. Plan {plan.nombreplan} | Hab. {plan.habitacion.calidad} | "
            f"Cap. {plan.habitacion.capacidad} personas | "
            f"${plan.habitacion.costonoche:,.0f}/noche | "
            f"Total {noches} noches: ${base:,.0f}{minibar_txt}")
    opcion = input("Elige un plan: ")
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(hotel.planes):
        plan = hotel.planes[opcion - 1]
        # Selección de minibar si el plan lo permite
        con_minibar = False
        if plan.habitacion.minibar:
          from utilidades import preguntar_si_no
          con_minibar = preguntar_si_no(
            f"¿Desea agregar minibar? (+${plan.habitacion.costo_minibar:,.0f}/noche) (s/n): "
          )
        return plan, con_minibar
      else:
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

# --- Flujo completo de una reserva ---
def flujo_reserva(cliente):
  ciudad        = seleccionar_ciudad()
  hotel         = seleccionar_hotel(ciudad)
  fecha_entrada, fecha_salida, noches = seleccionar_fechas(cliente, hotel)
  plan, con_minibar = seleccionar_plan(hotel, noches)
  costototal    = plan.costo_total(noches, con_minibar=con_minibar)

  reserva = Reserva(cliente, ciudad, hotel, plan,
                    fecha_entrada, fecha_salida, noches,
                    costototal, con_minibar=con_minibar)
  cliente.reservas.append(reserva)
  hotel.ocupar(1)

  print("\n--- RESERVA CONFIRMADA ---")
  reserva.mostrar()
