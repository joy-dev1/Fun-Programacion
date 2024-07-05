
def Par():
    n=int(input("Pon el numero: "))
    if n %2==0:
        return print(f"Verdadero el numero {n} es Par")
    else:
        return print(f"Falso el numero {n} es Par")
    
def Impar():
    n=int(input("Pon el numero: "))
    if n%2>0:
        return print(f"Verdadero el numero {n} es Impar")
    else:
        return print(f"Falso el numero {n} es Impar")
    
def AlmacenarLista():

    list=[]
    datos=int(input("Ponga cuantos numeros seran"))
    for i in range(datos):
        dato=int(input(f"Pon el numero {i} "))
    list.append(dato)
    return ParesLista(list)
def ParesLista():
    pares=[]
    for i in list():
        if i %2==0:
            print(f"Los numeros pares son {i}",end="")
            pares.append(i)
    return print(f"Estos son los numeros {pares} de la lista {list}")
def Pregunta():
    print("1. Saber si es par")
    print("2. Saber si es impar")
    print("3. Saber que numeros son pares")
    preg=int(input("Elige"))
    if preg ==1:
        Par()
    else:
        if preg==2:
            Impar()
        else:
            AlmacenarLista()

