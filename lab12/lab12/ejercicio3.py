ListaDatos=[]
def Agregar():
    dato=input("Ponga el texto que desea daber la longitud: ")
    ListaDatos.append(dato)
    longi2=len(ListaDatos)
    longi=list(map(len,ListaDatos))
    print(f"\tMENU")
    print("1. Ver la longitud de datos",end="|")
    print("2. Ver la longitud de caracteres")
    opcion=int(input("Elige: "))
    if opcion ==1:
        print(f"La longitud de datos es: \n{longi2}")
    else:
        print(f"La longitud de caracteres es: \n{longi}")
Agregar()





    


