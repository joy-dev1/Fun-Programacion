import datetime
fechaactual=datetime.datetime.now()

print(f"La fecha actual sera: \n {fechaactual}")

now = datetime.datetime.now()

formato_12h = now.strftime("%d-%m-%Y %I:%M:%S %p")

print(f"\n La fecha  y hora en formato de 12 horas sera: \n {formato_12h}")
