import random
import sys

lista_input = []
lista_random = []

print("Wprowadź 6 liczb od 1 do 49")
for i in range(0, 6):

    wprowadz = int(input())
    if wprowadz < 1 or wprowadz > 49:
        sys.exit("Zakres od 1 do 49")
    lista_input.append(wprowadz)

for i in range(0, 6):
    rand = random.randrange(1, 49)
    lista_random.append(rand)

print(lista_input)
print(lista_random)
count = 0

for i in range(0,6):
    if lista_input[i] in lista_random:
        count += 1

print("Udało ci się trafić : ", count)

