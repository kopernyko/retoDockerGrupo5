
alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
suspendidos = 0
aprobados = 0

for alumno in alumnos:
    print({alumno["nombre"].upper()})
    if alumno["nota"]>=5:
        print(f"El alumno ha aprobado. Con una nota de {alumno["nota"]}.")
        aprobados += 1
    else:
        print(f"El alumno ha suspendido. Con una nota de {alumno["nota"]}.")
        suspendidos += 1


def calcular_media(alumnos):
    """
    Calcula la media de las notas de los alumnos.
    """
    try:
        total_notas = sum(alumno["nota"] for alumno in alumnos)
        media = total_notas / len(alumnos)
    except ZeroDivisionError:
        print("0 alumnos en la lista. No se puede calcular la media.")
    return media

print(f"Número de alumnos aprobados: {aprobados}")
print(f"Número de alumnos suspendidos: {suspendidos}")
print(f"Total de alumnos: {len(alumnos)}")
print(f"Media de las notas: {calcular_media(alumnos)}")
