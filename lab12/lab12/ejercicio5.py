"""
5.	Elabore una funcion1() y una función2() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: funcion1([1,2,3,4]) debería imprimir 10 y funcion2([1,2,3,4]) debería devolver 24. 
"""
lista = [1,2,3,4]
def funcion1(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

def funcion2(lista):
    multiplicacion=1
    for i in lista:
        multiplicacion*=i
    return multiplicacion

print(f"El resultado de la suma de la lista es \n {funcion1(lista)}")
print(f"El resultado de la  multiplicacion de la lista \n{funcion2(lista)}")


