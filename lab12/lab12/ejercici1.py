
listaM=[]
def numeroMayor ():
    for i in range(3):
        numM=int(input(f"Ponga el numero {i+1}: "))
        listaM.append(numM)
    mayor=max(listaM)
    print(f"El numeor mayor es: \n {mayor}")
numeroMayor()


