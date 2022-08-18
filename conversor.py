#conversor de monedas de bolivares a otra
message = """ 
  Bienvenido a mi conversor, elija una opción para el resultado:
  1- Bolivares a dolares
  2- Bolivares a pesos Colombianos
  3- Bolivares a pesos Argentinos
  0- Salir
"""

def entry_text():
  user_input = float(input("Ingrese el monto en bolivares a consultar: "))
  return user_input

def printed_message(coin, value):
  total = entry_text() / value
  return f"seria un total de  {round(total, 2)} {coin}"


print(message)
option = int(input("Ingrese la opcion: "))

if option == 1:
  result = printed_message("Dolares", 6.1)
  print(result)
elif option == 2:
  result = printed_message("Pesos colombianos", 8)
  print(result)
elif option == 3:
  result = printed_message("Pesos Argentinos", 10)
  print(result)
else:
  print("Gracias por usar nuestro servicio :)")

