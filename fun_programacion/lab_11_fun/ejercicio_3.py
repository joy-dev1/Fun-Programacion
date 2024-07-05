import datetime

print("Ingrese la primera fecha en el formato: AAAA-MM-DD:")
fecha1_str = input()
print("Ingrese la segunda fecha en el formato: AAAA-MM-DD:")
fecha2_str = input()

fecha1 = datetime.datetime.strptime(fecha1_str, "%Y-%m-%d")
fecha2 = datetime.datetime.strptime(fecha2_str, "%Y-%m-%d")

diferencia = abs((fecha2 - fecha1).days)

print(f"\n La diferencia entre \n \t {fecha1_str} \n\t\ty \n\t{fecha2_str} es de \n\t{diferencia} días.")
