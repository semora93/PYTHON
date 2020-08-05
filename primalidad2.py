def run():
    numero = int(input("Escriba un número entero: "))
    div = numero - 1
    while div > 1:
        resid = numero % div
        if resid == 0:
            print("No es primo")
            break
        elif resid != 0:
            div -= 1
    if div == 1:
        print("Es primo")
    elif div == 0:
        print("No es primo")


if __name__ == "__main__":
    run()