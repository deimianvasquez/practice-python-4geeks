from functools import reduce

my_fruits = ["Manzana", "Pera", "Mango", "Mandarina","Cambur"]
my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]


# for num in my_list:
#   print(num)

# for fruit in my_fruits:
#   print(fruit)

# for index in range(len(my_list)):
#   print(index)


# count = 0
# while count < len(my_fruits):
#   print(my_fruits[count])
#   # count = count+1
#   count +=1

# salir = input("Ingresa una letra")
# while salir != "a":
#   print("Esta no es la letra de salir")
#   salir = input("Ingresa una letra: ")

def my_func(item):
  return f"Hola soy {item}"

#map
mapped_fruits = list(map(
  my_func,
  my_fruits
))
print(mapped_fruits)

def my_filt(item):
  return len(item) > 5

#filter 
filter_fruit = list(filter(
  my_filt,
  my_fruits
))
print(filter_fruit)

#reduce
my_reduce = reduce(
  lambda accu, current: accu + current,
  my_list,
  0
)
print(my_reduce)

my_tizana = reduce(
  lambda accu, current: f"{current}+{accu}",
  my_fruits,
  ""
)
print(my_tizana)