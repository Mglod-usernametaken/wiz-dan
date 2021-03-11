#zadanie 1

suma = 0
policz = input(u"Wprowadź zdowolne zdanie: \n")

print(policz.count('a'))

#zadanie 2

import sys
sys.stdout.write(u"podaj trzy liczby całkowite oddzielone spacjami")
liczby = sys.stdin.readline().split()
wynik = pow(int(liczby[0]), int(liczby[1])) + int(liczby[2])
print("a^b+c = ", wynik)

#zadanie 3

a = int(input("podaj liczbę a: \n"))
b = int(input("podaj liczbę b: \n"))
c = int(input("podaj liczbę c: \n"))
bestest = a

if b > a:
    if c > b:
        bestest = c
    else:
        bestest = b

elif c > a:
    bestest = c
print("największą liczbą jest", bestest)

#zadanie 4

listaNumerow = [1, 4, 9.8, 11, 4, 9.11, 13.13, 7, 0]
print(listaNumerow)

for index in range(len(listaNumerow)):
    listaNumerow[index] = pow(listaNumerow[index], 2)
print(listaNumerow)

#zadanie 5

cyferki = []
y = 0
while y<10:
    y +=1
    x = int(input("podaj liczbe:"))
    if (x%2) ==0:
        cyferki.append(x)

print(cyferki)
