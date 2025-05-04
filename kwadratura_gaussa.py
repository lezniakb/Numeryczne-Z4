import json
def GaussLaguerre(f, iloscWezlow):
    # przyblizenie calki e^(–x) * f(x) metoda Gaussa - Laguerre'a
    # przekazywana jest takze ilosc wezlow
    # podane wezly i wagi przekazane sa z literatury

    # przy wykorzystaniu znanych miejsc zerowych i wag wielomianow Laguerre'a wynik zapisujemy jako:
    # suma od i=1 do n, pod ktora stoi: w(i) f(x(i))
    # gdzie w(i) to wagi odpowiadajace danym wezlom
    # gdzie x(i) to wezly wielomianu Laguerre'a

    # wczytaj plik JSON z wprowadzonymi wezlami i odpowiadajacymi im wagami
    with open("wezly_wagi.json", "r") as file:
        data = json.load(file)

    # jesli ilosc wezlow nie pasuje, to nie wykonuj funkcji
    if iloscWezlow not in data:
        print("Liczba węzłów musi wynosić 2, 3, 4 lub 5")
        return None
    # np dla 2 wezlow: data[2]["wezly"]
    wezly = data[iloscWezlow]["wezly"]
    wagiWezlow = data[iloscWezlow]["wagiWezlow"]
    iloscIteracji = int(iloscWezlow)
    # obliczenie przyblizenia calki metoda Gaussa – Laguerre'a
    # "I" w przyblizeniu to suma od i=1 do n, pod ktora stoi: w(i) f(x(i))
    wynik = 0.0
    for i in range(iloscIteracji):
        wynik += wagiWezlow[i] * f(wezly[i])
    return wynik