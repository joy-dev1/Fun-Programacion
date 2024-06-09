
listaNotas = []
for i in range(10):
    nota = int(input(f"Ingrese la nota {i+1}: "))
    listaNotas.append(nota)
tuplaNotas = tuple(sorted(listaNotas, reverse=True))
listaFinal = list(tuplaNotas)
promedio = sum(listaFinal) / len(listaFinal)
for i in range(len(listaFinal)):
    if listaFinal[i] <= 10:
        listaFinal[i] = promedio
print(f"Las notas finales seran: \n {listaFinal}")
