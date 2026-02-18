import math


class Circulo:
    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0.")
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores que 0.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que 0.")
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores que 0.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:

        tol = 1e-9

        a = float(self.base)
        b = float(self.altura)
        c = float(self.calcular_hipotenusa())

        def eq(x: float, y: float) -> bool:
            return abs(x - y) <= tol

        if eq(a, b) and eq(b, c):
            return "Equilátero"
        elif eq(a, b) or eq(a, c) or eq(b, c):
            return "Isósceles"
        else:
            return "Escaleno"


class Rombo:
    def __init__(self, diagonal_mayor: float, diagonal_menor: float, lado: float):
        if diagonal_mayor <= 0 or diagonal_menor <= 0 or lado <= 0:
            raise ValueError("Diagonal mayor, diagonal menor y lado deben ser mayores que 0.")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado


class Trapecio:
    def __init__(self, base_mayor: float, base_menor: float, altura: float, lado1: float, lado2: float):
        if min(base_mayor, base_menor, altura, lado1, lado2) <= 0:
            raise ValueError("Todos los valores deben ser mayores que 0.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self) -> float:
        return (self.base_mayor + self.base_menor) * self.altura / 2

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2


def main():
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)
    figura5 = Rombo(10, 6, 5)
    figura6 = Trapecio(10, 6, 4, 5, 5)

    print("CÍRCULO")
    print("El área del círculo es =", figura1.calcular_area())
    print("El perímetro del círculo es =", figura1.calcular_perimetro())
    print()

    print("RECTÁNGULO")
    print("El área del rectángulo es =", figura2.calcular_area())
    print("El perímetro del rectángulo es =", figura2.calcular_perimetro())
    print()

    print("CUADRADO")
    print("El área del cuadrado es =", figura3.calcular_area())
    print("El perímetro del cuadrado es =", figura3.calcular_perimetro())
    print()

    print("TRIÁNGULO RECTÁNGULO")
    print("El área del triángulo es =", figura4.calcular_area())
    print("El perímetro del triángulo es =", figura4.calcular_perimetro())
    print("La hipotenusa del triángulo es =", figura4.calcular_hipotenusa())
    print("Tipo de triángulo:", figura4.determinar_tipo_triangulo())
    print()

    print("ROMBO")
    print("El área del rombo es =", figura5.calcular_area())
    print("El perímetro del rombo es =", figura5.calcular_perimetro())
    print()

    print("TRAPECIO")
    print("El área del trapecio es =", figura6.calcular_area())
    print("El perímetro del trapecio es =", figura6.calcular_perimetro())


if __name__ == "__main__":
    main()
