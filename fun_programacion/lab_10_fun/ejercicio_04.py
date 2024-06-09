clientes={}
menu="Principal"
opcion=0
while True:
    print(f"\n \t Menu")
    print("1. Registrar clientes")
    print("2. Mostrar clientes")
    print("3. Buscar Clientes")
    print("4. Actualizar clientes")
    print("5. Eliminar clientes")
    print("6. Salir")
    opcion=int(input(f"\n Elija: "))
    if opcion==1:
        empresa=input("Ponga la empresa: ")
        ruc=input("Ponga el RUC: ")
        clientes[empresa]=ruc
    elif opcion==2:
        print(f"\n Los clientes actuales son: \n{clientes} ")
    elif opcion==3:
        empresa=input(f"\n Ponga la empresa para buscar: ")
        if empresa in clientes:
            print(f"\n La empresa {empresa} si existe, su RUC es: {clientes[empresa]} ")
        else:
            print(f"\nLa empresa ingresada no existe, elija otra opcion")
    elif opcion==4:
        print(clientes)
        empresa=input(f"\n Ponga la empresa que desea actualizar: ")
        if empresa in clientes:
            ruc=input("Ponga el cambio de RUC: ")
            clientes[empresa]=ruc
            print(f"{empresa} Actualizado RUC a: \n{clientes[empresa]}")
        else:
            print(f"\nLa empresa ingresada no existe, elija otra opcion")
    elif opcion==5:
        print(clientes)
        eliminar=input("Ponga la empresa que desea eliminar: ")
        if eliminar in clientes:
            clientes.pop(eliminar)
            print(clientes)
        else:
            print(f"\nLa empresa ingresada no existe, elija otra opcion")
    elif opcion==6:
        break
    else:
        break