import math


def xKwadratWaga(x):
    #  f(x) = x^2 z wagą e^(-x)
    return math.exp(-x) * (x ** 2)

def xKwadrat(x):
    #  f(x) = x^2 bez wagi
    return x ** 2


def sinWaga(x):
    # f(x) = sin(x) z wagą e^(-x)
    return math.exp(-x) * math.sin(x)

def sinF(x):
    # f(x) = sin(x) bez wagi
    return math.sin(x)


def ulamekWaga(x):
    # f(x) = 1/(1+x^2) z wagą e^(-x)
    return math.exp(-x) / (1 + x ** 2)


def ulamek(x):
    # f(x) = 1/(1+x^2) bez wagi
    return 1 / (1 + x ** 2)


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
        "nazwa": "sin(x)",
        "zWaga": sinWaga,
        "bezWagi": sinF
    },
    "4": {
        "nazwa": "1/(1+x^2)",
        "zWaga": ulamekWaga,
        "bezWagi": ulamek
    }
}

def wybierzFunkcje():
    print("\nWybierz funkcję podcałkową:")
    print("1. f(x) = x^2")
    print("2. f(x) = x")
    print("3. f(x) = sin(x)")
    print("4. f(x) = 1/(1+x^2)")

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