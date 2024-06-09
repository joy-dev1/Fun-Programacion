"""8, 14, 19, 12, 10, 13, 10, 12, 11, 12, 13, 12, 17, 19, 12, 14, 11, 8, 12, 16

Elabore un programa que almacene en una tupla denominada notas los valores anteriores. Luego obtenga los siguientes datos:
•	Número de desaprobados (con nota menor a 13)
•	Número de aprobados (con nota 13 o superior)
"""

notas = (8, 14, 19, 12, 10, 13, 10, 12, 11, 12, 13, 12, 17, 19, 12, 14, 11, 8, 12, 16)
desaprobados = 0
aprobados = 0
for nota in notas:
    if nota < 13:
        desaprobados += 1
    else:
        aprobados += 1
print(f"El numero de alumnos desaprobados es: \n {desaprobados} ")
print(f"El numero de alumnos aprobados es: \n {aprobados}")
