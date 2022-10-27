# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby
#ujemnej, następuję wyjście z pętli.

while True:
    liczba = int(input("Podaj liczbę calkowitą: "))

    if liczba < 0:
        break