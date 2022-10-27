#Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
#tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue.

print("Podaj dwie liczby: jedną większą, drugą - mniejszą")
l1 = int(input("Podaj pierwszą liczbę: "))
l2 = int(input("Podaj drugą liczbę: "))
if l2 < l1:
    l1,l2 = l2,l1
while l1 <= l2:
    if l1 % 2 == 0:
        l1 += 1
        continue

    print(l1, end = " ")
    l1 += 1