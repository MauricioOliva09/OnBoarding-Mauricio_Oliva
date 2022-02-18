cadena = "Hola a todos este es un ejemplo de cadena"

# print(cadena.split())
print( cadena.strip())


# Datos
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

# Titulo genérico
titulo = f"facts about gravity of the {planet}'s {name} ".title()
print(titulo)

# Plantilla de cadena multilínea para contener el resto de la información
info = """------------------------------------------------
    Planet      Satellite       Gravity
------------------------------------------------"""
print(info)


print(titulo.join(info.format()))






from datetime import timedelta, datetime

def arrival_time(hours=51): #Se define argumento de palabra clave
    now = datetime.now()
    arrival = now + timedelta(hours=hours) #Se usa timedelta para permitir la operación de suma que da como resultado un objeto de hora nuevo
    return arrival.strftime('Arrival: %A %H:%M') # Devuelve la estimación arrival con formato de cadena