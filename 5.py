przesuniecie = int(input("Podaj klucz szyfru (przesuniecie): "))
tekst = input("Podaj tekst do zaszyfrowania: ")
tekst_zaszyfrowany = ""

for i in range(len(tekst)):
    znak = tekst[i]
    if znak.isupper():
        tekst_zaszyfrowany += chr((ord(znak) + przesuniecie - 65) % 26 + 65)
    else:
        tekst_zaszyfrowany += chr((ord(znak) + przesuniecie - 97) % 26 + 97)

print(tekst_zaszyfrowany)
