import math


def gauss_laguerre(f, n):
    """
    Oblicza przybliżenie całki postaci ∫₀∞ e^(–x) * f(x) dx metodą Gaussa–Laguerre’a
    dla zadanej liczby węzłów n (2, 3, 4 lub 5).

    W metodzie tej wagi i miejsca zerowe wielomianów Laguerre’a są znane z literatury.
    Wynik oblicza się jako sumę: suma_{i=1}^{n} [w_i * f(x_i)].
    """
    if n == 2:
        nodes = [0.585786437626905, 3.414213562373095]
        weights = [0.853553390593274, 0.146446609406726]
    elif n == 3:
        nodes = [0.4157745567834791, 2.2942803602790417, 6.289945082937479]
        weights = [0.711093009929173, 0.2785177335692408, 0.0103892565015861]
    elif n == 4:
        nodes = [0.3225476896193923, 1.7457611011583466, 4.536620296921128, 9.395070912301133]
        weights = [0.6031541043416336, 0.3574186924377997, 0.0388879085150055, 0.0005392947055613]
    elif n == 5:
        nodes = [0.2635603197181409, 1.4134030591065168, 3.596425771040722, 7.085810005858837, 12.64080084427578]
        weights = [0.5217556105828087, 0.3986668110831759, 0.0759424496817076, 0.00361175867992205,
                   0.000023369972385776]
    else:
        print("Liczba węzłów musi być 2, 3, 4 lub 5.")
        return None

    result = 0.0
    for i in range(n):
        result += weights[i] * f(nodes[i])
    return result


def gauss_legendre(f, a, b, n):
    """
    Oblicza przybliżenie całki ∫[a, b] f(x) dx metodą Gaussa–Legendre’a,
    przeskalowując przedział całkowania do standardowego przedziału [-1, 1].

    Procedura:
      1. Dla zadanego n (2, 3, 4 lub 5) korzystamy z literaturowo znanych węzłów (nodes) i wag (weights).
      2. Dokonujemy transformacji zmiennej: x = ((b – a)/2)*t + (a + b)/2, gdzie t ∈ [–1, 1].
      3. Wynik całki przybliża się wzorem: ((b–a)/2) * suma_{i=1}^{n}[w_i * f(x_i)].
    """
    if n == 2:
        nodes = [-0.5773502691896257, 0.5773502691896257]
        weights = [1.0, 1.0]
    elif n == 3:
        nodes = [-0.7745966692414834, 0.0, 0.7745966692414834]
        weights = [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
    elif n == 4:
        nodes = [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526]
        weights = [0.3478548451374538, 0.6521451548625461, 0.6521451548625461, 0.3478548451374538]
    elif n == 5:
        nodes = [-0.906179845938664, -0.5384693101056831, 0.0, 0.5384693101056831, 0.906179845938664]
        weights = [0.2369268850561891, 0.4786286704993665, 0.5688888888888889, 0.4786286704993665, 0.2369268850561891]
    else:
        print("Liczba węzłów musi być 2, 3, 4 lub 5.")
        return None

    result = 0.0
    # Transformacja zmiennej:
    # x = ((b – a)/2)*node + (a + b)/2, a dx = (b–a)/2 * dt.
    for i in range(n):
        x = ((b - a) / 2) * nodes[i] + ((a + b) / 2)
        result += weights[i] * f(x)
    result *= (b - a) / 2
    return result
