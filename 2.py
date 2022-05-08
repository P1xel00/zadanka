import sys
import statistics

lista_matematyka = []
lista_polski = []
lista_przyroda = []
print("Dostępne przedmioty matematyka, polski, przyroda")
wybor = input("Z którego przedmiotu chcesz wprowadzić oceny: ")
if wybor == "matematyka":
    lista = lista_matematyka
elif wybor == "polski":
    lista = lista_polski
elif wybor == "przyroda":
    lista = lista_przyroda
else:
    print("Nie ma takiego przedmiotu")
    sys.exit()


n = int(input("Ile ocen chcesz wprowadzić ? "))
if n == 0 or n < 0:
    sys.exit("Zero lub liczba ujemna")
print("Wprowadź oceny: ")
for i in range(0, n):

    wprowadz = int(input())
    if wprowadz > 6:
        sys.exit("Nie ma takich ocen w Polsce")
    lista.append(wprowadz)

print("Średnia ocen wynosi : ", sum(lista) / len(lista))
print("Mediana wynosi : ", statistics.median(lista))
print("Odchylenie standardowe wynosi : ", statistics.stdev(lista))
