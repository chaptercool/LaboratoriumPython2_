x = int(input("Podaj liczbę żeby wyświetlić gwiazdki: "))
str = ""
for i in range(x):
    for l in range(x):
        print("*", end=' ')
    print()