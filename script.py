#aquí haré cosas
from persona import Persona 
from espacio import Espacio
from utils import calcular_distancia,contar_personas_en_espacio
import utils

p_sevas = Persona("Sevas","2001-05-01")
p_aroa = Persona("Aroa","2002-05-01")
p_alvaro = Persona("Álvaro","2004-06-01")
print(p_sevas)

e_uax = Espacio("UAX Villanueva de la Cañada",50,50)
e_sevilla = Espacio("Sevilla",300,300)
print(e_uax)

e_sevilla.anadir_persona(p_alvaro)

e_uax.anadir_persona(p_sevas)
e_uax.anadir_persona(p_aroa)
numero_personas = utils.contar_personas_en_espacio(e_uax)

print(f"En {e_uax.nombre} hay {numero_personas} personas")