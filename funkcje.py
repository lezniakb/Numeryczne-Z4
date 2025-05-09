import math

def wielomian(x):
    # najlepszy do testowania kwadratur na przedziale skonczonym
    return x**3 - 2*x**2 + 2

def wielomianWaga(x):
    return math.exp(-x) * wielomian(x)

def xKwadratWaga(x):
    #  f(x) = x^2 z wagą e^(-x)
    return math.exp(-x) * (x ** 2)

def xKwadrat(x):
    #  f(x) = x^2 bez wagi
    return x ** 2


def eksponenta(x):
    #  f(x) = e^(-x/2)
    return math.exp(-x/2)

def eksponentaWaga(x):
    #  f(x) = e^(-x/2) z wagą e^(-x)
    return math.exp(-x) * eksponenta(x)

def xWaga(x):
    # f(x) = x z wagą e^(-x)
    return math.exp(-x) * x


def xF(x):
    # f(x) = x bez wagi
    return x

# slownik z funkcjami
dostepneFunkcje = {
    "1": {
        "nazwa": "x^2",
        "zWaga": xKwadratWaga,
        "bezWagi": xKwadrat
    },
    "2": {
        "nazwa": "x",
        "zWaga": xWaga,
        "bezWagi": xF
    },
    "3": {
        "nazwa": "x^3 - 2x^2 + 2",
        "zWaga": wielomianWaga,
        "bezWagi": wielomian
    },
    "4": {
        "nazwa": "e^(-x/2)",
        "zWaga": eksponentaWaga,
        "bezWagi": eksponenta
    }
}

def wybierzFunkcje():
    print("\nWybierz funkcję podcałkową:")
    print("1. f(x) = x^2")
    print("2. f(x) = x")
    print("3. f(x) = x^3 - 2x^2 + 2")
    print("4. f(x) = e^(-x/2)")

    wybor = input("Wybór [1-4]: ")

    if wybor in dostepneFunkcje:
        print(f"Wybrano funkcję f(x) = {dostepneFunkcje[wybor]['nazwa']}")
        return (
            dostepneFunkcje[wybor]["zWaga"],
            dostepneFunkcje[wybor]["bezWagi"]
        )
    else:
        print("Wpisano niewłaściwą cyfrę. Ustawiono: f(x) = x^2")
        return (
            dostepneFunkcje["1"]["zWaga"],
            dostepneFunkcje["1"]["bezWagi"]
        )
    print("\n")