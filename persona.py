class Persona:
    def __init__(self, nombre, fecha_de_nacimiento,posicion_x=0,posicion_y=0):
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        
    def __str__(self):
        return f"Nombre: {self.nombre}, posición: x={self.posicion_x} y={self.posicion_y}"
    
