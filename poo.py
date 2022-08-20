class Humano: ## crear una clase

  def __init__(self, nombre, apellido, edad, color_piel):
    self._nombre = nombre ## onjeto privado solo se modifica desde la misma clase (encapsulacion)
    self.apellido = apellido
    self.edad = edad
    self.color_piel = color_piel
    self.caminando = False


  def saludar(self):
    print(f"Hola {self._nombre} como estas {self.color_piel} ")


  def informacion(self):
    print(f"nombre: {self._nombre} \nApellido: {self.apellido} \nEdad: {self.edad} \nColor de piel: {self.color_piel} \nCaminando: {self.caminando}")


  def caminar(self, data):
    self.caminando = data

  def cambiar_nombre(self, nombre):
    self._nombre = nombre



class Trabajador(Humano):##herencia de una clase 

  def __init__(self, salario, profesion, humano_nombre, humano_apellido, humano_edad, humano_color_piel):

    super().__init__(humano_nombre, humano_apellido, humano_edad, humano_color_piel)## heredando el contructor

    self.salario = salario
    self.profesion = profesion

  # def informacion(self):
  #   print(f"nombre: {self.nombre} \nApellido: {self.apellido} \nEdad: {self.edad} \nColor de piel: {self.color_piel} \nCaminando: {self.caminando} \nSalario: {self.salario} \nProfesion: {self.profesion}")

  def informacion(self):
    super().informacion()## heredando el metodo
    print(f"Salario: {self.salario} \nProfesion: {self.profesion}")

#humano uno
humano_uno = Humano("Deimian", "Vasquez", 35, "marron")## instancia de la clase
humano_uno.informacion()

#humano dos
print(50*"*")
humano_dos = Humano("Octavio", "Lara", 19, "Rubio")
humano_dos.caminar(True)
humano_dos.cambiar_nombre("El que frao")
humano_dos.__nombre = "Hola que talllllllllllllllllll"
humano_dos.informacion()

#trabajador tres
print(50*"*")
# humano_tres = Trabajador("Ibrahim", "Other", 17, "catire")
trabajador_uno = Trabajador(1500, "presidente","Fernando", "Monnot", 53,"amrillo")
trabajador_uno.informacion()
print(50*"*")
trabajador_dos = Trabajador(5200, "Agricultor", "Carlos","Bracamonte", 26, "black")
trabajador_dos.informacion()
