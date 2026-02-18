from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    UA_KM = 149_597_870
    LIMITE_EXTERIOR_KM = UA_KM * 3.4

    def __init__(
        self,
        nombre: str,
        cantidad_satelites: int,
        masa: float,
        volumen: float,
        diametro: int,
        distancia_sol: int,   
        tipo: TipoPlaneta,
        es_observable: bool,
        periodo_orbital: float,   
        periodo_rotacion: float 
    ):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

        # Nuevos atributos
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self) -> None:
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")


        print(f"Periodo orbital (años) = {self.periodo_orbital}")
        print(f"Periodo de rotación (días) = {self.periodo_rotacion}")

    def calcular_densidad(self) -> float:
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        return self.distancia_sol > Planeta.LIMITE_EXTERIOR_KM


def main():
    p1 = Planeta(
        "Tierra",
        1,
        5.9736e24,
        1.08321e12,
        12742,
        150_000_000,
        TipoPlaneta.TERRESTRE,
        True,
        1.0,    
        1.0      
    )

    p2 = Planeta(
        "Júpiter",
        79,
        1.899e27,
        1.4313e15,
        139820,
        750_000_000,
        TipoPlaneta.GASEOSO,
        True,
        11.86, 
        0.41
    )

    p1.imprimir()
    print(f"Densidad del planeta = {p1.calcular_densidad()}")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
    print()

    p2.imprimir()
    print(f"Densidad del planeta = {p2.calcular_densidad()}")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}")


if __name__ == "__main__":
    main()
