alumnos={}
opcion2=0
opcion=0
menu_actual = 'Principal'
while True:
    if menu_actual == "Principal":
        print("\n \t Menu Principal")
        print(f"\n1. Opciones")
        print(f"\n2. Salir")
        opcion=int(input(f"\n Elige: "))
        if opcion == 1:
            menu_actual="Opciones"
        elif opcion == 2:
            print("Saliendo ")
            break
        else:
            print("Intentalo de nuevo")
    
    elif menu_actual == "Opciones":
            print(f"\n \t Menu Opciones")
            print(f"\n1. Agregar alumno")
            print(f"\n2. Obtener el numero de alumnos")
            print(f"\n3. Imprimir solo las claves")
            print(f"\n4. Imprimir solo los valores")
            print(F"\n5. Obtener el valor de un elemento dada su clave")
            print(f"\n6. Añadir un nuevo elemento al diccionario")
            print(f"\n7. Imprimir el diccionario con el nuevo elemento añadido")
            print(f"\n8. Emplear otro metodo para añadir valore sobre el diccionario")
            print(f"\n9. Eliminar un elemento del diccionario e imprimir los resultados de la nueva lista")
            print(f"\n10. Realizar una copia del diccionario")
            print(f"\n11. Eliminar los elementos del diccionario")
            opcion2=int(input(f"\n Elige: "))
            if opcion2 ==1:
                num_al=int(input(f"\nPonga el numero de alumnos a agregar: "))
                for n in range(1,num_al+1):
                    codigo=input(f"Ingrese el codigo del alumno: {n}: ")
                    apellido=input("Ingrese el apellido: ")
                    alumnos[codigo]=apellido
                print(f"\t La lista actual sera: {alumnos}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2 == 2:
                cantidad=len(alumnos)
                print(f"\n El numero de alumnos es: {cantidad} ")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break  
            elif opcion2 ==3:
                claves=alumnos.keys()
                print(f"\n Las claves de los alumonos es: {claves}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==4:
                valores=alumnos.values()
                print(f"\n Los valores de los alumnos son: {valores}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==5:
                clave=input(f"\n Ponga la clave para la busqueda: ")
                if clave in alumnos:
                    print(f"\n La clave {clave} si esta en el diccionario y su valor es: {alumnos[clave]} ")
                else:
                    print(f"\n La clave que ingresaste no se encuentra en el diccionario")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==6:
                codigo=input(f"Ingrese el codigo del alumno: ")
                apellido=input("Ingrese el apellido: ")
                alumnos[codigo]=apellido
                print(f"\t La lista actual sera: {alumnos}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==7:
                print(f"\n El diccionario actualmente es : \n {alumnos}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==8:
                codigo=input(f"Ingrese el codigo del alumno: ")
                apellido=input("Ingrese el apellido: ")
                alumnos.update({codigo:apellido})
                print(f"\t La lista actual sera: {alumnos}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==9:
                codigo=input(f"\n Ponga el elemento que desea eliminar")
                print(f"\n Lista actual es: {alumnos}")
                if codigo in alumnos:
                    alumnos.pop(codigo)
                    print(f"\n La lista sin la clave {codigo} sera: {alumnos}")
                else:
                    print(f"\n El codigo NO EXISTE")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==10:
                copia_Alumnos=alumnos.copy()
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            elif opcion2==11:
                copia_Alumnos=alumnos.copy()
                print(f"\n1. {alumnos}")
                print(f"2. {copia_Alumnos}" )
                eliminar=int(input("Eliga de cual diccionario se eliminaran los valores: "))
                if eliminar==1:
                    alumnos.clear()
                    print(f"\n Los valores de diccionario se eliminaron actualmente eseta asi : {alumnos}")
                else:
                    copia_Alumnos.clear()
                    print(f"\n Los valores de diccionario se eliminaron actualmente eseta asi : {copia_Alumnos}")
                print(f"\n 1. Ver menu anterior")
                print(f"\n 2. Salir")
                consulta=int(input("Elige: "))
                if  consulta==1:
                    menu_actual="Opciones"
                else:
                    break
            else:
                break






