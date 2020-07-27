print("Hola, a través de este programa vamos a saber si tienes un peso saludable")
gender = input("¿Cuál es tu género? (M = Masculino; F = Femenino; O = Otro): ")
if gender == "M":
    pesoM = int(input("Por favor digita tu peso en Kg: "))
    if pesoM > 80:
        print("Tu peso está un poco elevado")
    elif pesoM < 50:
        print("Tu peso es muy bajo")
    else:
        print("Tu peso es ideal, qué guapo te ves")
elif gender == "F":
    pesoF = int(input("Por favor digita tu peso en Kg: "))
    if pesoF > 70:
        print("Tu peso está un poco elevado")
    elif pesoF < 40:
        print("Tu peso es muy bajo")
    else:
        print("Tu peso es ideal, qué guapa te ves")
elif gender == "O":
    pesoO = int(input("Por favor digita tu peso en Kg: "))
    if pesoO > 75:
        print("Tu peso está un poco elevado")
    elif pesoO < 45:
        print("Tu peso es muy bajo")
    else:
        print("Tu peso es ideal, qué bien")
else:
    print("Has seleccionado mal tu género, qué bestia")