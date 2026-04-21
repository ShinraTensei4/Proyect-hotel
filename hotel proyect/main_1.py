# ============================================================
# main_1.py — Punto de entrada del sistema hotelero
# Gestiona el registro/reconocimiento de clientes,
# el menú de sesión y el ciclo principal del programa.
# La lógica de reservas está en reservaciones.py
# ============================================================

from clientes import Cliente, clientes
from utilidades import preguntar_si_no
from reservaciones import flujo_reserva

# --- Ingreso y validación del nombre del cliente ---
def pedir_nombre():
  while True:
    nombrecliente = input("Ingrese su nombre: ").strip()
    if nombrecliente == "":
      print("El nombre no puede estar vacío.")
    elif not nombrecliente.replace(" ", "").isalpha():
      print("El nombre NO puede contener números ni caracteres especiales.")
    else:
      return nombrecliente

# --- Ingreso y validación del DNI ---
def pedir_dni():
  while True:
    dni = input("Ingrese su DNI: ").strip()
    if dni == "":
      print("El DNI no puede estar vacío.")
    elif not dni.isdigit():
      print("El DNI NO puede contener letras.")
    elif len(dni) < 6:
      print("El DNI es muy corto (mínimo 6 dígitos).")
    elif len(dni) > 10:
      print("El DNI es inválido (máximo 10 dígitos).")
    else:
      return dni

# --- Verificación DNI y nombre en el sistema ---
def registrar_cliente():
  print("\n========================================")
  print("       BIENVENIDO AL SISTEMA")
  print("========================================")

  # Ingreso nombre
  nombrecliente = pedir_nombre()

  # Ingreso DNI
  dni = pedir_dni()

  # Verificación DNI: existe en sistema
  for c in clientes:
    if c.dni == dni:
      if c.nombrecliente.lower() == nombrecliente.lower():
        # DNI y nombre coinciden → cliente recurrente reconocido
        print(f"\nCliente reconocido. ¡Bienvenido de nuevo, {c.nombrecliente}!")
        return c, True
      else:
        # DNI existe pero con nombre diferente → error de identidad
        print("Ya existe un cliente registrado con ese DNI pero diferente nombre.")
        print("Verifique sus datos e intente de nuevo.")
        return registrar_cliente()

  # Verificación nombre: mismo nombre, diferente DNI
  for c in clientes:
    if c.nombrecliente.lower() == nombrecliente.lower() and c.dni != dni:
      print("Ya existe un cliente con ese nombre pero diferente DNI.")
      print("Use un nombre diferente o verifique su DNI.")
      return registrar_cliente()

  # Cliente nuevo → registrar
  cliente = Cliente(nombrecliente, dni)
  clientes.append(cliente)
  return cliente, False

# --- Menú para clientes recurrentes ---
def menu_cliente_recurrente(cliente):
  while True:
    print(f"\n--- MENÚ DE {cliente.nombrecliente.upper()} ---")
    print("1. Ver mis reservas")
    print("2. Realizar una nueva reserva")
    print("3. Cerrar sesión")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
      # Ver reservas registradas del cliente
      if not cliente.reservas:
        print("No tiene reservas registradas aún.")
      else:
        print(f"\n--- RESERVAS DE {cliente.nombrecliente} ---")
        for i, r in enumerate(cliente.reservas, start=1):
          print(f"\nReserva #{i}")
          r.mostrar()

    elif opcion == "2":
      return True   # Ir a realizar reserva

    elif opcion == "3":
      return False  # Cerrar sesión

    else:
      print("Opción inválida. Elija 1, 2 o 3.")

# --- Ciclo de sesión de un cliente ---
def sesion_cliente(cliente, es_recurrente):
  if es_recurrente:
    # Menú completo para cliente con historial
    while True:
      hacer_reserva = menu_cliente_recurrente(cliente)
      if hacer_reserva:
        flujo_reserva(cliente)
        if not preguntar_si_no("\n¿Desea realizar otra reserva? (s/n): "):
          break
      else:
        break
  else:
    # Cliente nuevo: va directo al flujo de reserva
    flujo_reserva(cliente)
    while preguntar_si_no("\n¿Desea realizar otra reserva? (s/n): "):
      flujo_reserva(cliente)

# --- Ciclo principal del sistema ---
def main():
  while True:
    cliente, es_recurrente = registrar_cliente()
    sesion_cliente(cliente, es_recurrente)
    # Al terminar la sesión vuelve al inicio sin perder datos
    print("\nSesión cerrada. Volviendo al inicio del sistema...")

main()
