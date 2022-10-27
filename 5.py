#Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
#liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
#wykorzystaniem pętli while.

n = int(input("Proszę podać ilość studentów: "))
a = 1 #wyświetlanie od pierwszego studenta
c = 0 #podstawienie pod dodawanie punktów

while a <= n:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    c += b #sumowanie punktów studentów
    a += 1 #przechodzenie do kolejnego studenta
y = c / n #obliczanie średniej
print("Średnia wszystkich studentów: ", y)