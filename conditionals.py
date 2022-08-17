# color = input("Ingresa el color: ")

# name = "None"
# lastname = "Vasquez"
# my_list = ["Octavio", "Deimian", "Juan"]
# age = False
# person = 101

# if "Octavo" in my_list:
#   print("Si esta en la lista negra")
# else:
#   print("No esta")


# if name is None:
#   print("Esto no tiene nada es NONE")
# else:
#   print(f"Este el el valor {name}")


# if color == "blue":
#   print("Odio ese color")
# else:
#   print("Cool ese color")


# if name == "deimian" or lastname =="Vasquez":
#   print("respuesta positiva")
# else:
#   print("respuesta negativa")


# if age:
#   print("El true")

# else:
#   print("El false rick")


# if person >=20 and person<=100:
#   print("estas en el rango")


# if person <= 20:
#   print("Te sale emn 100$")
# elif person <= 50:
#   print("te sale en 200$")
# elif person <= 100:
#   print("te sale en 230$")
# else:
#   print("Super caro todo")


#conversor de monedas de bolivares a otra
message = """ 
  Bienvenido a mi conversor, elija una opción para el resultado:
  1- Bolivares a dolares
  2- Bolivares a pesos Colombianos
  3- Bolivares a pesos Argentinos
  0- Salir
"""

print(message)
option = int(input("Ingrese la opcion: "))

if option == 1:
  my_change = float(input("Ingrese el monto en bolivares a consultar: "))
  total = my_change / 6.1
  print(f"seria un total de  {round(total, 2)} Dolares")
elif option == 2:
  my_change = float(input("Ingrese el monto en bolivares a consultar: "))
  total = my_change / 8
  print(f"seria un total de  {round(total, 2)} Pesos colombianos")
elif option == 3:
  my_change = float(input("Ingrese el monto en bolivares a consultar: "))
  total = my_change / 10
  print(f"seria un total de  {round(total, 2)} Pesos Argentinos")
else:
  print("Gracias por usar nuestro servicio :)")

