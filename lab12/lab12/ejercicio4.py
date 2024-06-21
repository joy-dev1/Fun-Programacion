
def vocal():
    vocal=input(f"Ponga una letra: \n")
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        reslt=True
    else:
        reslt=False
    return print(f"¿La letra {vocal} es una vocal?\n"+" "+str(reslt)) 

vocal()


