# zadanie 1

calkowita1 = 7
calkowita2 = 13
zmiennoprzecinkowa1 = 1.0
zmiennoprzecinkowa2 = 0.3
znakowa1 = "hamak"
znakowa2 = 'f'
zespolona1 = 7 + 8j
zespolona2 = -8j

print(calkowita1,
      calkowita2, '\n',
      zmiennoprzecinkowa1,
      zmiennoprzecinkowa2, '\n',
      znakowa1,
      znakowa2, '\n',
      zespolona1,
      zespolona2
      )

# #zadanie 2

a = 1
a += 5
a -= 3
a *= 8
a /= 3
a **= 2
a %= 12
print(a)

# zadanie 3

import math

print(pow(math.e, 10))
iks = 5 + pow(math.sin(8), 2)
print(pow(iks, (1 / 6)))
print("whatever that symbols mean")

# zadanie 4

imie = "JORGE"
nazwisko = "BUCHFINK"

print(imie.capitalize(), "von", nazwisko.capitalize())

# zadanie 5

piosenka = "Daft Punk - Around the World: \n"
for i in range(0, 72):
    piosenka += "Around the world, around the world \n"

print("piosenka", piosenka[0:28], "zawiera", piosenka.count("world"), "slow \"world\".")

# zadanie 6

motto = "What doesn't kill You makes you pstrąger"
print("motto[0] = ", motto[0])
print("motto [ostatni] = ", motto[-1])
# gdyby nie ujemne indeksy, mozna uzyc print(motto[len(motto)-1])

# zadanie 7

poszatkowany = motto.split()
print(poszatkowany)

# zadanie 8

slowo = u"tłuszcz"
przecinek = 0.12
hexadec = 61
print("string: %(a)s\nfloat: %(b)f\nhexadecimal: %(c)x" % {'a':slowo, 'b':przecinek, 'c':hexadec})

# zadanie 9

sporty = []
for i in range(0,5):
      sporty.append(input("podaj swoje ulubione sporty: \n"))
sporty.reverse()
for i in range(0,3):
      sporty.append(input("teraz wymien kilka nielubianych sportow:\n"))

print("wymieniles: ", sporty)

# zadanie 10

slownik = {"ww":u"wyżej wymieniony", "l":"lat", "str":"strona", "dr":"doktor", "mgr":"magister", "inz":u"inżynier"}
print(slownik[input("podaj skrot do rozwiniecia: ")])