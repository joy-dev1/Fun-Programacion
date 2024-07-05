from fun_numeros import *
"""
1.	Elabore un módulo que almacene tres funciones:
•	Que retorne verdadero si el número ingresado es par,caso contrario falso
•	Que retorne verdadero si el número ingresado es impar,caso contrario falso
•	Que retorne los numeros pares de un intervalo
"""

"""
print( f'\t'+ 'Menu'+'\n'+ '1.- Saber si es par '+'\n' + '2.- Saber si es impar'+'\n' + '3.- Saber de intervalos de numeros ' )
eleccion=int(input('Elige:  '))
if eleccion ==1:
    num1=int(input('Pon un numero para saber si es par: ' ))
    print(fun_numeros.par(num1))
elif eleccion==2:
    num1=int(input('Pon un numero para saber si es impar: ' ))
    print(fun_numeros.impar(num1)) 
elif eleccion==3:
    num1=int(input('Pon el primer numero de inicio del intervalo: ' ))
    num2=int(input('Pon el numero del final del intervalo: ' ))
    print(fun_numeros.interPares(num1, num2))  
"""


"""
2.	Elabore un módulo que almacene una función que tome como argumento dos números enteros y devuelva el mayor.
"""

"""
num1=int(input('Ponga el primer numero: '))
num2=int(input('Ponga el segundo numero: '))

fun_numeros.mayor(num1,num2)

"""


"""
3.	Elabore un módulo que almacene una función que calcule la longitud de una expresión de texto ingresada por teclado. 
"""
"""
dato=input("Ponga el texto que desea daber la longitud: ")

fun_numeros.Agregar(dato)

"""


"""
4.	Elabore un módulo llamado operaciones que almacene dos funciones: funcion_suma() y función_prod() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: funcion_suma() ([1,2,3,4]) debería imprimir 10 y función_prod ([1,2,3,4]) debería devolver 24. 
"""
"""
print('MENU')
print('1.- Sumar los numeros de la lista'+ '\n'+'2.- Multiplicar los numeros de la lista' )

eleccion=int(input('Elige:  '))
listNum=[1,2,3,4]
if eleccion==1:
    fun_numeros.suma(listNum)    
elif eleccion==2:
    fun_numeros.prod(listNum)
"""


"""
5.	Elabore un módulo que almacene tres funciones: 
a.	Una función que imprima la serie de fibonacci,
b.	Una función que imprima la suma de la serie de fibonacci
c.	Una función que imprima el factorial de un número
"""
"""
num=int(input('Ponga el numero para \n 1.- Imprimir la serie fibonacci, \n 2.- Suma de la serie de fibonacci y \n 3.- El factorial del numero \n : '))
print("Serie de Fibonacci:")
fun_numeros.serie_fibonacci(num)
fun_numeros.suma_fibonacci(num)
fun_numeros.factorial(num)
"""


linea('*',20)
print()
cuadro('*', 8, 20)


