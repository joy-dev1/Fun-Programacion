"""
6.	Implemente un programa Python, el cual incluirá una función linea con el siguiente encabezado: linea(car_izq, car_centro, car_der, tam), esta función podrá trazar una línea horizontal como se muestra en el siguiente ejemplo, se podrán especificar 3 caracteres para armar el trazado de la línea, carácter izquierdo, carácter central, carácter derecho y tam indica el tamaño total de la línea:
"""

def linea(car_izq, car_centro, car_der, tam):
    num_centro = tam - 2
    print()
    linea = car_izq + car_centro * num_centro + car_der
    print(linea)

def caracter():
    
    car_izq=input("Ponga el caracter izquierdo: ")
    car_centro=input("Ponga el caracter en medio: ")
    car_der=input("Ponga el caracter derecho: ")
    tam=int(input("Ponga el tamaño de toda la linea: "))
    linea(car_izq,car_centro,car_der,tam)    

caracter()









