class Mascota:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color


class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    # Método para sonido
    def sonido(self):
        print("Los perros ladran")


class PerroGrande(Perro):
    razas_permitidas = ['pastor alemán', 'doberman', 'rotweiller']

    def __init__(self, nombre, edad, color, peso, muerde, raza):
        if raza not in self.razas_permitidas:
            raise ValueError(f"Raza {raza} no permitida para Perro Grande")
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza


class PerroMediano(Perro):
    razas_permitidas = ['collie', 'dálmata', 'bulldog', 'galgo', 'sabueso']

    def __init__(self, nombre, edad, color, peso, muerde, raza):
        if raza not in self.razas_permitidas:
            raise ValueError(f"Raza {raza} no permitida para Perro Mediano")
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza


class PerroPequeno(Perro):
    razas_permitidas = ['caniche', 'yorkshire terrier', 'schnauzer', 'chihuahua']

    def __init__(self, nombre, edad, color, peso, muerde, raza):
        if raza not in self.razas_permitidas:
            raise ValueError(f"Raza {raza} no permitida para Perro Pequeño")
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza


class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    # Método para sonido
    def sonido(self):
        print("Los gatos maúllan y ronronean")


class GatoSinPelo(Gato):
    razas_permitidas = ['esfinge', 'elfo', 'donskoy']

    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        if raza not in self.razas_permitidas:
            raise ValueError(f"Raza {raza} no permitida para Gato Sin Pelo")
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza


class GatoPeloLargo(Gato):
    razas_permitidas = ['angora', 'himalayo', 'balinés', 'somalí']

    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        if raza not in self.razas_permitidas:
            raise ValueError(f"Raza {raza} no permitida para Gato de Pelo Largo")
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza


class GatoPeloCorto(Gato):
    razas_permitidas = ['azul ruso', 'británico', 'manx', 'devon rex']

    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        if raza not in self.razas_permitidas:
            raise ValueError(f"Raza {raza} no permitida para Gato de Pelo Corto")
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza


class PruebaMascotas:

    def ejecutar_pruebas(self):
        print("=== Pruebas de Perros ===")
        try:
            perro_grande = PerroGrande("Rex", 5, "Negro", 40, True, "pastor alemán")
            print(f"Perro Grande: {perro_grande.nombre}, Raza: {perro_grande.raza}")
            perro_grande.sonido()
        except ValueError as e:
            print(e)

        try:
            perro_mediano = PerroMediano("Max", 3, "Blanco", 20, False, "collie")
            print(f"Perro Mediano: {perro_mediano.nombre}, Raza: {perro_mediano.raza}")
            perro_mediano.sonido()
        except ValueError as e:
            print(e)

        try:
            perro_pequeno = PerroPequeno("Toby", 2, "Marrón", 5, False, "chihuahua")
            print(f"Perro Pequeño: {perro_pequeno.nombre}, Raza: {perro_pequeno.raza}")
            perro_pequeno.sonido()
        except ValueError as e:
            print(e)

        try:
            PerroGrande("Thor", 4, "Gris", 50, True, "beagle")
        except ValueError as e:
            print(f"Error al crear Perro Grande: {e}")

        print("\n=== Pruebas de Gatos ===")
        try:
            gato_pelo_largo = GatoPeloLargo("Luna", 3, "Blanco", 1.5, 2.0, "angora")
            print(f"Gato Pelo Largo: {gato_pelo_largo.nombre}, Raza: {gato_pelo_largo.raza}")
            gato_pelo_largo.sonido()
        except ValueError as e:
            print(e)

        try:
            gato_pelo_corto = GatoPeloCorto("Milo", 2, "Gris", 1.0, 1.5, "azul ruso")
            print(f"Gato Pelo Corto: {gato_pelo_corto.nombre}, Raza: {gato_pelo_corto.raza}")
            gato_pelo_corto.sonido()
        except ValueError as e:
            print(e)

        try:
            gato_sin_pelo = GatoSinPelo("Sphynx", 4, "Rosa", 1.2, 1.8, "esfinge")
            print(f"Gato Sin Pelo: {gato_sin_pelo.nombre}, Raza: {gato_sin_pelo.raza}")
            gato_sin_pelo.sonido()
        except ValueError as e:
            print(e)

        try:
            GatoPeloLargo("Simba", 3, "Naranja", 1.5, 2.0, "siamés")
        except ValueError as e:
            print(f"Error al crear Gato Pelo Largo: {e}")


# Ejecutar las pruebas
if __name__ == "__main__":
    prueba = PruebaMascotas()
    prueba.ejecutar_pruebas()