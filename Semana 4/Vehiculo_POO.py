class Vehiculo:
    def __init__(self, color, ruedas):      # Inicializa un vehículo con color y número de ruedas.
        self.color = color
        self.ruedas = ruedas

    def __str__(self):  # Devuelve la descripción general del vehículo.
        return f"Color: {self.color}, {self.ruedas} ruedas, Tipo: {type(self).__name__}"


class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindraje):   # Inicializa un coche con color, velocidad y cilindraje.
        super().__init__(color, ruedas=0)  # Un coche siempre tiene 4 ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):      # Devuelve la descripción específica del coche.
        return f"Color: {self.color}, {self.velocidad} km/h, {self.ruedas} ruedas, {self.cilindraje} cc, Tipo: {type(self).__name__}"


class Moto(Vehiculo):
    def __init__(self, color):      # Inicializa una moto con color.
        super().__init__(color, ruedas=2)  # Una moto siempre tiene 2 ruedas


# Pruebas del programa
print("================== PRUEBAS ==================")

# Crear y mostrar un coche
coche = Coche(color="azul", velocidad=150, cilindraje=1200)
print(coche)

# Crear y mostrar una moto
moto = Moto(color="rojo")
print(moto)

# Crear y mostrar un vehículo genérico
vehiculo = Vehiculo(color="verde", ruedas=3)
print(vehiculo)
