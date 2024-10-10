#módulo
def calcular_distancia(persona1,persona2):
    #raiz ((persona1_x - persona2_x)^2 + (persona1_y - persona2_y)^2)
    distancia = ((persona1.posicion_x - persona2.posicion_x)**2
     + (persona1.posicion_y - persona2.posicion_y)**2)**0.5
    return distancia 

def contar_personas_en_espacio(espacio):
    lista_personas = espacio.personas # [persona1, persona2,...,personaX]
    numero_personas = len(lista_personas) #int
    return numero_personas
