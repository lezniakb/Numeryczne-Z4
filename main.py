import math
from newton_cotes import calkaSimpsona, calkujDoNieskonczonosci
from kwadratura_gaussa import gauss_laguerre, gauss_legendre

# funkcja podcalkowa
def funPodcalkowa(x):
    return math.exp(-x) * (x ** 2)

# wybrane f(x) dla metody Gaussa (wariant 3): f(x)=x^2
def fxDoGaussa(x):
    return x ** 2

dostepne_wybory = ["0", "1", "2", "3", "4"]
while True:
    print(f"----------------------------\nWybierz metodę całkowania:\n"
    "1. Kwadratura Newtona–Cotesa (Simpsona) na przedziale skończonym\n"
    "2. Kwadratura Newtona–Cotesa (Simpsona) – całka niewłaściwa [0, +∞)\n"
    "3. Kwadratura Gaussa–Laguerre’a dla całki ∫₀∞ e^(–x)*x² dx\n"
    "4. Kwadratura Gaussa–Legendre’a (przeskalowana) – całkowanie na przedziale [a,b]\n"
    "0. Zakończ program.\n----------------------------")
    wybor = input("Wybierz opcję: ")

    if wybor == "0":
        exit(0)

    if wybor not in dostepne_wybory:
        print("Wybrano niewłaściwą opcję!")
        input("Wciśnij Enter aby kontynuować...")
        continue

    dokladnosc = float(input("Podaj wymaganą dokładność (np. 0.0001): "))

    if wybor == "1":
        a = float(input("Podapj oczątek przedziału: "))
        b = float(input("Podaj koniec przedziału: "))
        wynik = calkaSimpsona(funPodcalkowa, a, b, dokladnosc)
        print("----------------------------")
        print(f"Wynik całkowania metodą Newtona–Cotesa:", end=" ")

    elif wybor == "2":
        a = float(input("Podaj wartość początkową 'a' dla przedziału [0, a): "))
        delta = float(input("Podaj długość przedziału 'δ': "))
        wynik = calkujDoNieskonczonosci(funPodcalkowa, a, delta, dokladnosc)
        print("----------------------------")
        print(f"Wynik całkowania całki niewłaściwej metodą Newtona–Cotesa:", end=" ")

    elif wybor == "3":
        n = int(input("Podaj liczbę węzłów (2, 3, 4 lub 5): "))
        wynik = gauss_laguerre(fxDoGaussa, n)
        print("----------------------------")
        print(f"Wynik całkowania metodą Gaussa–Laguerre’a:", end=" ")

    elif wybor == "4":
        a = float(input("Podaj początek przedziału całkowania (np. 0): "))
        b = float(input("Podaj koniec przedziału całkowania (np. 1): "))
        n = int(input("Podaj liczbę węzłów (2, 3, 4 lub 5): "))
        wynik = gauss_legendre(funPodcalkowa, a, b, n)
        print("----------------------------")
        print(f"Wynik całkowania metodą Gaussa–Legendre’a:", end=" ")

    print(wynik)
