usuarios={}
menu="Principal"

while True:
    if menu=="Principal":
        email=input(f"Ponga el email: ")
        if email in usuarios:
            print(f"\nEste usuario ya existe, intente nuevamente")
            menu="Principal"
        else:
             menu="Menu2"
    elif menu=="Menu2":     
        password=input("Ingrese el password: ")
        usuarios[email]=password
        print(f"\n ¿Desea salir?")
        print(f"\n1.- Si")
        print(f"\n2.- No")
        consulta=int(input("Elige: "))
        if  consulta==1:
            print(f"\n Todos los usuarios actualmente son: {usuarios}")
            break
        elif consulta==2:
            menu="Principal"  
        else:
                break



                