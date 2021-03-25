# Marcin Głód, Wizualizacja Danych, sem 2, gr2

# zadanie 1
import math
rownanie1 = (1/2)**2
rownanie2 = ((math.sqrt(3))/2)**2
print("%.2f" %(rownanie1 + rownanie2))

rownanie3 = math.sin(25)+ (math.e)**5
print("%.2f" % (pow(rownanie3, (1/4))))

# zadanie 2


tekst = "Lorem ipsum dolor sit amet eleifend at, feugiat at, mattis varius. In hac habitasse platea dictumst. Cum sociis natoque penatibus et dui. Aliquam risus at est. Pellentesque dolor. In commodo volutpat aliquam convallis. Fusce venenatis consequat. Integer sodales sed, ultrices bibendum, sem in sapien. Cras justo augue eget nibh sit amet, libero. Class aptent taciti sociosqu ad litora torquent per inceptos hymenaeos. Pellentesque orci sem leo ac augue. Sed fringilla metus, quis ante. Duis quam ipsum, ultricies porta. Vivamus consequat hendrerit. Donec tempus vitae, vestibulum tincidunt congue. Maecenas tincidunt. Proin nonummy laoreet, purus eu nunc sem, rutrum id, vehicula enim. "

male = 0
duze = 0
cyfry = 0
for i in tekst:
    if i.islower():
        male += 1
    if i.isupper():
        duze += 1
    if i.isdigit():
        cyfry += 1
print("male litery:", male, "\nduze litery:", duze, "\ncyfry:", cyfry )

# zadanie 3


plik = open('vat.txt', 'a+')
netto = input("podaj cene netto:")
vat = input("podaj stawke vat:")
flaga = 0
try:
    netto = float(netto)
except:
    print("cena netto nie jest poprawna liczba")


try:
    vat = float(vat)

except:
    print("stawka VAT nie jest poprawna liczba")

try:
    brutto = netto * (1 + (vat / 100))
    plik.write("cena netto towaru(PLN) %(a).2f, stawka VAT: %(b).2f, cena brutto %(c).2f" % {'a': netto, 'b': vat,
                                                                                             'c': brutto})
except:
    print("cos poszlo nie tak. sprobuj ponownie.")
plik.close()
