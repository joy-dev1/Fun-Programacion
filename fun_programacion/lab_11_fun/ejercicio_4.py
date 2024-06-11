import datetime

print("Ingrese la fecha de inicio en el formato AAAA-MM-DD:")
fecha_inicio = input()
print("Ingrese la fecha de fin en el formato AAAA-MM-DD:")
fecha_fin = input()

fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
fecha_fin = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")

fecha_actual = fecha_inicio
domingos = []

while fecha_actual <= fecha_fin:
    if fecha_actual.weekday() == 6: 
        domingos.append(fecha_actual)
    fecha_actual += datetime.timedelta(days=1)

print(f"Los dias domingos entre \n {fecha_inicio} \n\t y \n{fecha_fin}:")
for domingo in domingos:
    print(domingo.strftime("%Y-%m-%d"))

print(f"El total de domingos son: {len(domingos)}")
