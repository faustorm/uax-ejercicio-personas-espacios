class Espacio:
    def __init__(self,nombre,largo=10,ancho=10):
        self.nombre = nombre
        self.personas = []
        self.largo = largo
        self.ancho = ancho

    def anadir_persona(self,persona):
        self.personas.append(persona)
        print(f"He añadido a {persona.nombre} al espacio {self.nombre}")

    def __str__(self):
        return f"Este espacio es: {self.nombre} y mide {self.ancho} metros por {self.largo} metros"