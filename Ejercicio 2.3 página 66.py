from enum import Enum


class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"


class TipoAutomovil(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"


class Automovil:
    def __init__(
        self,
        marca: str,
        modelo: int,
        motor: float,  
        tipo_combustible: TipoCombustible,
        tipo_automovil: TipoAutomovil,
        numero_puertas: int,
        cantidad_asientos: int,
        velocidad_maxima: int,  
        color: Color,
        automatico: bool,  
        valor_multa: int = 200_000,  
    ):
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color

        self._automatico = automatico  
        self._velocidad_actual = 0


        self._valor_multa = valor_multa
        self._cantidad_multas = 0

   
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value: str):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value: int):
        self._modelo = value

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value: float):
        self._motor = value

    @property
    def tipo_combustible(self):
        return self._tipo_combustible

    @tipo_combustible.setter
    def tipo_combustible(self, value: TipoCombustible):
        self._tipo_combustible = value

    @property
    def tipo_automovil(self):
        return self._tipo_automovil

    @tipo_automovil.setter
    def tipo_automovil(self, value: TipoAutomovil):
        self._tipo_automovil = value

    @property
    def numero_puertas(self):
        return self._numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, value: int):
        self._numero_puertas = value

    @property
    def cantidad_asientos(self):
        return self._cantidad_asientos

    @cantidad_asientos.setter
    def cantidad_asientos(self, value: int):
        self._cantidad_asientos = value

    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, value: int):
        self._velocidad_maxima = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: Color):
        self._color = value

    @property
    def automatico(self):
        return self._automatico

    @automatico.setter
    def automatico(self, value: bool):
        self._automatico = bool(value)

    @property
    def velocidad_actual(self):
        return self._velocidad_actual

    @velocidad_actual.setter
    def velocidad_actual(self, value: int):
        if value < 0:
            print("No se puede establecer una velocidad negativa.")
            return
        if value > self._velocidad_maxima:
            print("No se puede establecer una velocidad superior a la máxima del automóvil.")
            return
        self._velocidad_actual = value


    def tiene_multas(self) -> bool:
        return self._cantidad_multas > 0

    def valor_total_multas(self) -> int:
        return self._cantidad_multas * self._valor_multa

    def _generar_multa(self):
        self._cantidad_multas += 1
        print(
            f" Multa generada por intentar exceder la velocidad máxima. "
            f"Multas acumuladas: {self._cantidad_multas}"
        )


    def acelerar(self, incremento_velocidad: int):
        """
        Si al acelerar se supera la velocidad máxima, NO se aumenta la velocidad,
        pero se genera una multa (y se incrementa cada intento).
        """
        nueva = self._velocidad_actual + incremento_velocidad
        if nueva <= self._velocidad_maxima:
            self._velocidad_actual = nueva
        else:
            self._generar_multa()
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def desacelerar(self, decremento_velocidad: int):
        nueva = self._velocidad_actual - decremento_velocidad
        if nueva >= 0:
            self._velocidad_actual = nueva
        else:
            print("No se puede desacelerar a una velocidad negativa.")

    def frenar(self):
        self._velocidad_actual = 0

    def tiempo_estimado_llegada(self, distancia_km: float) -> float:
        if self._velocidad_actual == 0:
            raise ZeroDivisionError("No se puede calcular el tiempo estimado con velocidad actual = 0.")
        return distancia_km / self._velocidad_actual

    def imprimir(self):
        print("----- Datos del Automóvil -----")
        print(f"Marca: {self._marca}")
        print(f"Modelo (año): {self._modelo}")
        print(f"Motor (L): {self._motor}")
        print(f"Tipo de combustible: {self._tipo_combustible.value}")
        print(f"Tipo de automóvil: {self._tipo_automovil.value}")
        print(f"Número de puertas: {self._numero_puertas}")
        print(f"Cantidad de asientos: {self._cantidad_asientos}")
        print(f"Velocidad máxima (km/h): {self._velocidad_maxima}")
        print(f"Color: {self._color.value}")
        print(f"Automático: {'Sí' if self._automatico else 'No'}")
        print(f"Velocidad actual (km/h): {self._velocidad_actual}")
        print(f"¿Tiene multas?: {'Sí' if self.tiene_multas() else 'No'}")
        print(f"Total multas: {self.valor_total_multas():,} COP")


def main():
    auto1 = Automovil(
        marca="Ford",
        modelo=2018,
        motor=3.0,
        tipo_combustible=TipoCombustible.DIESEL,
        tipo_automovil=TipoAutomovil.EJECUTIVO,
        numero_puertas=5,
        cantidad_asientos=6,
        velocidad_maxima=250,
        color=Color.NEGRO,
        automatico=True, 
        valor_multa=200_000,
    )

    auto1.imprimir()

    auto1.velocidad_actual = 240
    auto1.acelerar(5)    
    auto1.acelerar(10)   
    auto1.acelerar(50)  

    print("Velocidad actual =", auto1.velocidad_actual)
    print("Tiene multas =", auto1.tiene_multas())
    print("Total multas =", auto1.valor_total_multas())


if __name__ == "__main__":
    main()
