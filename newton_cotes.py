def wzorSimpsona(f, a, b, n):
    # oblicza wartosc calki w przedziale [a, b] metoda simpsona
    # n musi byc parzyste i jest liczba podprzedzialow

    # n musi byc parzyste, wiec w razie gdy nie jest - zwieksz o 1
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    # suma poczatkowa = wartosc funkcji na krancach przedzialu
    s = f(a) + f(b)

    # sumowanie wartosci funkcji w punktach
    for i in range(1, n):
        # przejdz przez wszystkie "n"
        # jezeli wartosc jest nieparzysta, to waga = 4,
        if i % 2 == 1:
            s += 4 * f(a + i * h)

        # jezeli wartosc jest parzysta, to waga = 2
        else:
            s += 2 * f(a + i * h)

    return s * h / 3


def calkaSimpsona(f, a, b, dokladnosc):
    # oblicz wartosc calki w przedziale [a, b]
    # liczba poprzedzialow iteracyjnie jest zwiekszana do osiagniecia podanej dokladnoscadnosci

    # poczatkowa liczba podprzedzialow (musi byc parzysta)
    n = 2
    wynik = wzorSimpsona(f, a, b, n)

    while True:
        # zwiekszamy liczbe podprzedzialow (moze byc przez pomnozenie razy 2)
        n *= 2
        nowyWynik = wzorSimpsona(f, a, b, n)
        # jesli osiagnelismy dokladnosc to zwroc wynik i zakoncz dzialanie
        if abs(nowyWynik - wynik) < dokladnosc:
            return nowyWynik
        wynik = nowyWynik


def calkujDoNieskonczonosci(f, a, delta, dokladnosc):
    # oblicz wartosc calki niewlasciewej z uwzglednieniem granic
    # ∫[0, +∞) f(x) dx metodą Newtona–Cotesa (wzór Simpsona)
    """
    Krok po kroku
      1. Oblicz calke poczatkowoa na przedziale [0, a)
      2. Dla kolejnych przedzialow [a, a+δ), [a+δ, a+2δ) ... oblicz wartość całki.
      3. Jesli wartosc calki nie miesci sie w dokladnosci, to jest ona dodawana do wyniku,
         a przedzial jest przesuwany.
       3b. Jesli wartosc calki juz miesci sie w dokladnosci, to przyjmujemy,
           ze dalszy wklad całki w wynik jest znikomy.
    """
    # calka na poczatkowym przedziale [0, a)
    wynik = calkaSimpsona(f, 0, a, dokladnosc)
    x = a
    
    while True:
        # oblicz kolejna calke z nastepnego przedzialu
        # np. jesli pierwszy to byl [0, 2), to nastepny to [2, 2+delta)
        nastepnyWynik = calkaSimpsona(f, x, x + delta, dokladnosc)
        # jesli osiagniemy dokladnosc to zwroc wynik
        if abs(nastepnyWynik) < dokladnosc:
            return wynik
        wynik += nastepnyWynik
        x += delta