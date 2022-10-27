#Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
#mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby

l1 = int(input("Podaj pierwszą liczbę: "))
l2 = int(input("Podaj drugą liczbę: "))
if l2 < l1:
    l1,l2 = l2,l1
while l1 <= l2:
    print(l1, end = " ")
    l1 += 1