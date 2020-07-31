print("""
Hola, este programa ayudará a detectar si debes gastar dinero o no en un antojo determinado.
Para ello tendremos en cuenta variables como tu salario mensual, el valor estimado de tu antojo, las compras que hayas hecho anteriormente, y la relevancia de tu antojo.
Por favor sigue las instrucciones e introduce la información necesaria como se te indica.
""")

def calculo_antojo(salario1, valor_antojo1, compras_previas1, valor_compras_previas1, relevancia_antojo1):
    if salario1 < valor_antojo1*5:
        print("No deberías comprar ese antojo, es muy caro.")
    elif compras_previas1 == "Sí":
        if valor_compras_previas1 >= valor_antojo1:
            print("No compres ese antojo, ya ha sido suficiente por ahora.")
        elif relevancia_antojo1 <= 2:
            print("El antojo no vale la pena, no lo hagas.")
        elif relevancia_antojo1 <= 4:
            print("Puedes comprar el antojo pero piénsalo muy bien: quizás no es lo mejor ahora mismo.")
        elif relevancia_antojo1 > 4:
            print("Está bien, de verdad quieres ese antojo, cómpralo.")
        else:
            print("Hiciste algo mal, por favor vuelve a empezar y asegúrate de escribir todo bien.")
    elif relevancia_antojo1 <= 2:
        print("El antojo no vale la pena, no lo hagas.")
    elif relevancia_antojo1 <= 4:
        print("Puedes comprar el antojo pero piénsalo muy bien, quizás no es lo mejor ahora mismo.")
    elif relevancia_antojo1 > 4:
        print("Está bien, de verdad quieres ese antojo, cómpralo.")
    else:
        print("Hiciste algo mal, por favor vuelve a empezar y asegúrate de escribir todo bien.")

salario = int(input("Digita tu salario mensual (sólo números, no incluyas decimales): "))
valor_antojo = int(input("Ahora ingresa el valor del antojo que deseas comprar (sólo números, no incluyas decimales): "))
compras_previas = input("¿Has comprado antojos en los últimos 30 días? (Responde 'Sí' o 'No'): ")

if compras_previas == "Sí":
    valor_compras_previas = int(input("¿Cuál fue el valor de ese antojo? (sólo números, no incluyas decimales): "))
else:
    valor_compras_previas = 0

relevancia_antojo = int(input("En una escala de 1 a 5, donde 1 equivale a 'insignificante' y 5 a 'esencial', ¿cómo calificarías tu deseo por este antojo?: "))

calculo_antojo(salario, valor_antojo, compras_previas, valor_compras_previas, relevancia_antojo)