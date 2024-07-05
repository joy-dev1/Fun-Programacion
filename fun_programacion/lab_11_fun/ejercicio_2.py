import datetime

continuar = True

while continuar:
    print(f"\n \t Elija una opcion")
    print("1. Obtener fecha y hora en formato de 12 horas")
    print("2. Obtener fecha y hora en formato de 24 horas")
    print("3. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == '1':
        ahora = datetime.datetime.now()
        formato_12_horas = ahora.strftime("%Y-%m-%d %I:%M:%S %p")
        print("Fecha y hora en formato de 12 horas:", formato_12_horas)
    elif opcion == '2':
        ahora = datetime.datetime.now()
        formato_24_horas = ahora.strftime("%Y-%m-%d %H:%M:%S")
        print("Fecha y hora en formato de 24 horas:", formato_24_horas)
    elif opcion == '3':
        print("Saliendo ")
        continuar = False
    else:
        print("Esta opcion no es validad, intentelo mas tarde")
