lista=[]
n=int(input("Ponga la cantidad de datos para agregar a la lista: "))
print("----------------------------------------------------")
contador=0
while range(n):
    numeros = int(input("Ponga el valor : "))
    lista.append(numeros)
    contador+=1
    if contador==n:
        break


for num in lista:
    
    suma = sum(lista)
    promedio = suma / len(lista)
    num_mayor=max(lista)
    num_menor=min(lista)


cadena_num = ' + '.join(map(str,lista))
print("---------------------------------------------------")
print(f"La suma de : \n" + "\t"+ str(cadena_num)+"\n\t" +"=" +"\n"+"\t" + str(suma))
print("---------------------------------------------------")
print("El promedio de la suma de: \n"+ str(cadena_num) + "\n" + "/" + "\n"+ str(len(lista))+ "\n"+ "="+ "\n"+ str(promedio))
print("---------------------------------------------------")
print("El numero mayor es: \n" + str(num_mayor))
print("El numero menor es: \n" + str(num_menor))








