import sys

lista = []

n = int(input("Ile liczb chcesz wprowadzić ? "))
if n == 0 or n < 0:
    sys.exit("Zero lub liczba ujemna")

print("Wprowadź liczby: ")

for i in range(0, n):

    wprowadz = int(input())
    lista.append(wprowadz)

for i in range(0,n ):
    print("Indeks: ", i," Element: ", lista[i])
lista.reverse()
print("Odwrócona lista", lista)
lista.sort()
print("Posortowana lista", lista)
usun_element = int(input("Jaki element chcesz usunąć ? (usuwa tylko pierwsze wystąpienie) "))
lista.remove(usun_element)
print(lista)
usun_indeks = int(input("Jaki indeks chcesz usunąć ? "))
del lista[usun_indeks]
print(lista)
wybierz = int(input("Podaj element którzy chcesz policzyć i uzyskac pierwszy indeks "))
count = 0
for i in lista:
    if i == wybierz:
        count += 1
print("Ten element występuje tyle razy: ", count)
print("Indeks pierwszego wystąpienia podanego elementu: ", lista.index(wybierz))
indeks_i = int(input("Podaj pierwszy indeks: "))
indeks_j = int(input("Podaj drugi indeks: "))
if indeks_j < indeks_i:
    sys.exit("Drugi indeks musi być większy")
print(lista[indeks_i:indeks_j])