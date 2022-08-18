import random
#cuandop el juego aranca la maquina debe elegit entre 9 números
#luego pregunta solicita al usuario que agregue tres números
# si se aciertas el numero pero no la posición  cuanta como un herido
#si se aciertas la posicion y el número cuenta como un muerto 
#ganas si aciertas tres numeros


lista_numeros = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(lista_numeros)
seleccion_maquina = lista_numeros[0:3]

while True:
  muertos = 0
  heridos = 0

  entrada_usuario = input("Ingrese tres números: ")
  if len(entrada_usuario) !=3:
    print("Por favor son tres NÚMEROS PANA: ")
    continue

  seleccion_usuario = []
  for num in entrada_usuario:
    seleccion_usuario.append(int(num))

  for index_maquina, valor_maquina in enumerate(seleccion_maquina):
    for index_usuario, valor_usuario in enumerate(seleccion_usuario):
      if index_maquina == index_usuario and valor_maquina == valor_usuario:
        muertos += 1
      elif valor_usuario == valor_maquina:
        heridos += 1
  
  print(f"Tienes {muertos} muertos y {heridos} heridos")
  if muertos == 3:
    print("GANASTESSSS HEEEEE !!!!!")
    break

