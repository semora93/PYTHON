def run():
    numero = int(input("Escriba por favor un número entero: "))
    if numero != 2 and numero != 3:
        resid1 = numero % 2
        resid2 = numero % 3
        if resid1 == 0 or resid2 == 0:
            print("No es primo")
        elif resid1 > 0 and resid2 > 0:
            print("Es primo")


if __name__ == "__main__":
    run()