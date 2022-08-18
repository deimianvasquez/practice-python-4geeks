def suma(num1, num2):
  return num1+num2
  

def saludar(nombre, saludo): #args, kwargs
  result = f"{saludo} {nombre}"
  return result


print(suma(52,52))
print(saludar(saludo="Hola como estas", nombre="Deimian"))

saludar_dos = lambda nombre, saludo: f"{saludo} {nombre}"
#nombre_funcion = lambda parametros: return
suma_dos = lambda num1,num2: num1+num2

print(suma_dos(50,25))
print(saludar_dos("Octavio", "Hey broth"))

def prueba(num1, num2):
  print(str(num1) + str(num2))

prueba(9,9)



def suma(a,b):
  return a+b

def multiplicar(a,b):
  return a*b

resultado = multiplicar(suma(3,5),suma(1,1))
print(resultado)


