print("Hola, ésta es una aplicación para convertir pesos colombianos (COP) a dólares (USD)")
cop = input("Por favor ingresa el monto de pesos (COP) a convertir: ")
cop = float(cop)
usd = cop / 3700
usd = str(usd)
cop = str(cop)
print("Tus " + cop + " COP equivalen a " + usd + " USD")