def run():
    print("Hola, este programa te ayudará a realizar una pruba de primalidad para todos los números en un intervalo determinado.")
    comienzo_rango = int(input("Ingresa el número entero que denota el comienzo del rango deseado: "))
    final_rango = int(input("Ahora ingresa el número entero que denota el final del rango deseado (el rango incluirá este número): "))
    rango_usuario = list(range(comienzo_rango, final_rango + 1))
    for i in rango_usuario:
        div = i - 1
        while div > 1:
            resid = i % div
            if resid == 0:
                print(str(i) + " no es primo")
                break
            elif resid != 0:
                div -= 1
        if div == 1:
            print(str(i) + " es primo")
        elif div == 0:
            print(str(i) + " no es primo")


if __name__ == "__main__":
    run()