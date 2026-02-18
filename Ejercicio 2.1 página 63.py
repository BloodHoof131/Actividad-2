class Persona:

    def __init__(self, nombre: str, apellidos: str,
                 numero_documento: str, anio_nacimiento: int,
                 pais_nacimiento: str, genero: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Número de documento de identidad =", self.numero_documento)
        print("Año de nacimiento =", self.anio_nacimiento)
        print("País de nacimiento =", self.pais_nacimiento)
        print("Género =", self.genero)
        print()


def main():
    p1 = Persona(
        "Pedro", "Pérez", "1053121010",
        1998, "Colombia", "H"
    )

    p2 = Persona(
        "Luis", "León", "1053223344",
        2001, "Colombia", "H"
    )

    p1.imprimir()
    p2.imprimir()


if __name__ == "__main__":
    main()
