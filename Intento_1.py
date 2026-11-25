class Flor:
    def __init__(self, nombre, tipo_flor, color, numero_petalos):
        self.nombre = nombre
        self.tipo_flor = tipo_flor
        self.color = color
        self.numero_petalos = numero_petalos

    def mostrar_datos(self):
        return f"{self.nombre} ({self.tipo_flor}) - {self.color}, {self.numero_petalos} petalos"


# HERENCIA
class FlorExotica(Flor):
    def __init__(self, nombre, tipo_flor, color, numero_petalos, origen):
        super().__init__(nombre, tipo_flor, color, numero_petalos)
        self.origen = origen

    def mostrar_origen(self):
        return f"Origen de la flor: {self.origen}"

    def mostrar_datos(self):
        return f"{super().mostrar_datos()} - Origen: {self.origen}"


# AGREGACION
class Floristeria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.flores = []

    def agregar_flor(self, flor):
        self.flores.append(flor)

    def mostrar_flores(self):
        print(f"\nFlores de la floristeria {self.nombre}:")
        for i, flor in enumerate(self.flores, start=1):
            print(f"{i}. {flor.mostrar_datos()}")

    def contar_flores(self):
        return len(self.flores)


# OPCION 1: REGISTRAR FLORES
def registrar_flores(floristeria):
    nombre = input("Escriba el nombre de su flor: ")
    tipo_flor = input("Escriba el tipo de flor: ").strip().lower()
    color = input("Escriba el color de la flor: ")
    numero_de_petalos = int(input("Escriba el numero de petalos de su flor: "))

    flor1 = Flor(nombre, tipo_flor, color, numero_de_petalos)

    if numero_de_petalos >= 25:
        tipo_correcto = "rosa"
        cantidad = "muchos"
    elif numero_de_petalos >= 9:
        tipo_correcto = "girasol"
        cantidad = "una cantidad intermedia de"
    else:
        tipo_correcto = "lirio"
        cantidad = "pocos"

    if tipo_flor == tipo_correcto:
        print(f"Correcto. Tiene {cantidad} pétalos, su flor es: {tipo_flor}")
    else:
        print(f"Tiene {cantidad} pétalos, por lo tanto no es un {tipo_flor}, es un {tipo_correcto}")

    print("\nRegistre una flor exotica:")
    nombre2 = input("Escriba el nombre de la flor: ")
    tipo2 = input("Escriba el tipo de flor: ")
    color2 = input("Escriba el color: ")
    petalos2 = int(input("Escriba el numero de petalos: "))
    origen = input("Escriba el lugar de origen: ")

    flor2 = FlorExotica(nombre2, tipo2, color2, petalos2, origen)

    floristeria.agregar_flor(flor1)
    floristeria.agregar_flor(flor2)
    print("\nFlores registradas con exito.")


# OPCION 2: VER FLORES REGISTRADAS
def ver_flores(floristeria):
    if floristeria.contar_flores() == 0:
        print("\nAun no hay flores registradas.")
    else:
        floristeria.mostrar_flores()
        print("Total de flores:", floristeria.contar_flores())


# MENU PRINCIPAL
def menu():
    floristeria1 = Floristeria("Las Rosas")

    while True:
        print("\n===== MENU =====")
        print("1. Registrar flores")
        print("2. Ver flores registradas")
        print("3. Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            registrar_flores(floristeria1)
        elif opcion == "2":
            ver_flores(floristeria1)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")


menu()

#Cambio en linea 115 para presentacion

luis esta aca si

