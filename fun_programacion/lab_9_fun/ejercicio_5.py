
n = int(input("Ingrese la cantidad de nnmeros que desea registrar: "))

num_lista = []

contador = 0
while range(n):
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    num_lista.append(numero)
    contador += 1
    if contador==n:
        break

# Imprimir los números en orden invertido
print("Los números en orden invertido son:")
indice = n - 1
while indice >= 0:
    print(num_lista[indice])
    indice -= 1
