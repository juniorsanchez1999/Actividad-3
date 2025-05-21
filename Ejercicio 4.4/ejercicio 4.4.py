# Clase Persona
class Persona:
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion

    # Métodos para obtener y establecer el nombre
    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, valor: str) -> None:
        self._nombre = valor

    # Métodos para obtener y establecer la dirección
    def get_direccion(self) -> str:
        return self._direccion

    def set_direccion(self, valor: str) -> None:
        self._direccion = valor


# Clase Estudiante (hereda de Persona)
class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    # Métodos para obtener y establecer la carrera
    def get_carrera(self) -> str:
        return self._carrera

    def set_carrera(self, valor: str) -> None:
        self._carrera = valor

    # Métodos para obtener y establecer el semestre
    def get_semestre(self) -> int:
        return self._semestre

    def set_semestre(self, valor: int) -> None:
        self._semestre = valor


# Clase Profesor (hereda de Persona)
class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    # Métodos para obtener y establecer el departamento
    def get_departamento(self) -> str:
        return self._departamento

    def set_departamento(self, valor: str) -> None:
        self._departamento = valor

    # Métodos para obtener y establecer la categoría
    def get_categoria(self) -> str:
        return self._categoria

    def set_categoria(self, valor: str) -> None:
        self._categoria = valor


# Clase Universidad (gestión de personas)
class Universidad:
    def __init__(self):
        self._estudiantes = []
        self._profesores = []

    def agregar_estudiante(self, estudiante: Estudiante) -> None:
        self._estudiantes.append(estudiante)

    def agregar_profesor(self, profesor: Profesor) -> None:
        self._profesores.append(profesor)

    # Métodos para obtener las listas de estudiantes y profesores
    def get_estudiantes(self) -> list:
        return self._estudiantes

    def get_profesores(self) -> list:
        return self._profesores


# Bloque principal del programa
if __name__ == "__main__":
    # Crear estudiantes y profesores
    estudiante1 = Estudiante("Juan", "Calle 123", "Ingeniería", 3)
    estudiante2 = Estudiante("Ana", "Calle 456", "Medicina", 2)
    profesor1 = Profesor("Dr. Pérez", "Calle 789", "Ciencias", "Titular")
    profesor2 = Profesor("Dra. Gómez", "Calle 101", "Matemáticas", "Asociada")

    # Crear universidad y agregar personas
    universidad = Universidad()
    universidad.agregar_estudiante(estudiante1)
    universidad.agregar_estudiante(estudiante2)
    universidad.agregar_profesor(profesor1)
    universidad.agregar_profesor(profesor2)

    # Mostrar estudiantes
    print("Estudiantes:")
    for estudiante in universidad.get_estudiantes():
        print(f"Nombre: {estudiante.get_nombre()}, Carrera: {estudiante.get_carrera()}, Semestre: {estudiante.get_semestre()}")

    # Mostrar profesores
    print("\nProfesores:")
    for profesor in universidad.get_profesores():
        print(f"Nombre: {profesor.get_nombre()}, Departamento: {profesor.get_departamento()}, Categoría: {profesor.get_categoria()}")