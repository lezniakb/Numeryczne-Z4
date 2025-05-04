import math
from newton_cotes import calkaSimpsona, calkujDoNieskonczonosci
from kwadratura_gaussa import GaussLaguerre

# funkcja podcalkowa
def funPodcalkowa(x):
    return math.exp(-x) * (x ** 2)

# wybrane f(x) dla metody Gaussa (wariant 3): f(x)=x^2
def fxDoGaussa(x):
    return x ** 2

dostepne_wybory = ["0", "1", "2", "3"]
while True:
    print(f"----------------------------\nWybierz metodę całkowania:\n"
    "1. Kwadratura Newtona–Cotesa (Simpsona) na przedziale skończonym\n"
    "2. Kwadratura Newtona–Cotesa (Simpsona) – całka niewłaściwa [0, +∞)\n"
    "3. Kwadratura Gaussa–Laguerre’a dla całki ∫₀∞ e^(–x)*x² dx\n"
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
        iloscWezlow = input("Podaj liczbę węzłów (2, 3, 4 lub 5): ")
        # uwaga: iloscWezlow jest typu string aby odczytywac wezly z pliku JSON
        wynik = GaussLaguerre(fxDoGaussa, iloscWezlow)
        print("----------------------------")
        if wynik is None:
            print("Funkcja nie zwróciła wyniku.")
            continue
        print(f"Wynik całkowania metodą Gaussa–Laguerre’a:", end=" ")
        # Uwaga!!
        # Przy ilosci wezlow 5, przy wezle nr. 5 jest niezgodnosci podanej wagi ostatniego wezla.
        # Wyklad: 0.000032
        # Inne zrodla (w tym literatura): 0.000023 (dokladniej: 0.00002337, dokładniej: 0.0000233670)
        # mowa tu o wezle "12.640801"

    print(wynik)

# to do:
"""
1. Zrobic wiecej funkcji i dac wybor uzytkownikowi
2. sprawdzic wezel 5 w ilosci wezlow 5
"""