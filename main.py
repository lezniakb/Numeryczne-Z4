from newton_cotes import calkaSimpsona, calkujDoNieskonczonosci
from kwadratura_gaussa import GaussLaguerre
from funkcje import wybierzFunkcje

dostepne_wybory = ["0", "1", "2", "3"]
while True:
    print(f"----------------------------\nWybierz metodę całkowania:\n"
    "1. Kwadratura Newtona–Cotesa (wzór Simpsona) na przedziale skończonym\n"
    "2. Kwadratura Newtona–Cotesa (wzór Simpsona) – całka niewłaściwa [0, +∞)\n"
    "3. Kwadratura Gaussa–Laguerre’a [0, +∞) z wagą e^(-x)\n"
    "0. Zakończ program.\n----------------------------")
    wybor = input("Wybierz opcję [0-3]: ")

    if wybor == "0":
        exit(0)

    if wybor not in dostepne_wybory:
        print("Wybrano niewłaściwą opcję!")
        input("Wciśnij Enter aby kontynuować...")
        continue

    FunWaga, funBezWagi = wybierzFunkcje()

    n = 0
    if wybor == "1":
        a = float(input("Podaj początek przedziału: "))
        b = float(input("Podaj koniec przedziału: "))
        dokladnosc = float(input("Podaj wymaganą dokładność [np. 0.0001]: "))
        wynik, n = calkaSimpsona(FunWaga, a, b, dokladnosc)
        print("----------------------------")
        print(f"Wynik całkowania metodą Newtona–Cotesa:", end=" ")

    elif wybor == "2":
        a = float(input("Podaj wartość początkową 'a' dla przedziału [0, a): "))
        delta = float(input("Podaj długość przedziału 'δ': "))
        dokladnosc = float(input("Podaj wymaganą dokładność [np. 0.0001]: "))
        wynik, n = calkujDoNieskonczonosci(FunWaga, a, delta, dokladnosc)
        print("----------------------------")
        print(f"Wynik całkowania całki niewłaściwej metodą Newtona–Cotesa:", end=" ")

    elif wybor == "3":
        iloscWezlow = input("Podaj liczbę węzłów [2, 3, 4 lub 5]: ")
        # uwaga: iloscWezlow jest typu string aby odczytywac wezly z pliku JSON
        wynik = GaussLaguerre(funBezWagi, iloscWezlow)
        print("----------------------------")
        if wynik is None:
            print("Funkcja nie zwróciła wyniku.")
            continue
        print(f"Wynik całkowania metodą Gaussa–Laguerre’a:", end=" ")

    print(wynik)

    if n != 0:
        print(f"n = {n}")