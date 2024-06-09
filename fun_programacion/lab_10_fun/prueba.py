# Estado inicial para el menú principal
menu_actual = "principal"

while True:
    if menu_actual == "principal":
        print("\nMenu Principal")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Submenú")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("Has seleccionado Opción 1")
        elif opcion == '2':
            print("Has seleccionado Opción 2")
        elif opcion == '3':
            menu_actual = "submenu"
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
    
    elif menu_actual == "submenu":
        print("\nSubmenú")
        print("1. Subopción 1")
        print("2. Subopción 2")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("Has seleccionado Subopción 1")
        elif opcion == '2':
            print("Has seleccionado Subopción 2")
        elif opcion == '3':
            menu_actual = "principal"
        else:
            print("Opción no válida, intente de nuevo.")
