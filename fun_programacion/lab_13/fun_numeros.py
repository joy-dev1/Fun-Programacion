def par(num):
    return num % 2 == 0
def impar(num):
    return num % 2 != 0
def interPares(ini, fin):
    pares = []
    for num in range(ini, fin + 1):
        if par(num):
            pares.append(num)
    return pares
def mayor(num1,num2):
    if num1 > num2:
        print(f'El numero {num1} es mayor')
    else:
        print(f'El numero {num2} es mayor')


def Agregar(dato):
    ListaDatos=[]
    ListaDatos.append(dato)
    longi=list(map(len,ListaDatos))
    print(f"La longitud es: \n{longi}")

def suma(listNum):
 
    suma=sum(listNum)
    print(f'La suma de la lista {listNum} es : \n {suma} ')
def prod(listNum):
    pruductoNum=1
    for n in listNum:
        pruductoNum*= n
    print(f'La multiplicaion de la lista {listNum} es \n {pruductoNum}')

def serie_fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        print(a, end=' ')
        a, b = b, a + b
    print() 

def suma_fibonacci(num):
    a, b = 0, 1
    suma = a
    for i in range(1, num):
        a, b = b, a + b
        suma += a
    print(f"La suma de los primeros {num} numeros de la serie de fibonacci es: \n {suma}")

def factorial(num):
    if num == 0 or num == 1:
        print(f"El factorial de {num} es: 1")
        return
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    print(f"El factorial de {num} es: \n {resultado}")

def linea(car,tam):
    print(car*tam)

def cuadro(car, nfil, ncol):
    linea(car, ncol)
    for i in range(nfil-2):
        print(car + ' '*(ncol-2) + car)
    linea(car, ncol)



