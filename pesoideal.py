print("""Hola, gracias a este programa podrás decidir cuándo es un buen momento para pedir algún antojo de comida grasosa.
Tendremos en cuenta factores como qué día de la semana es, si ya has consumido comida grasosa en la semana y si presentas algún malestar digestivo.
""")

def consumo():
    if consumo_previo == "Sí":
        print("No sigas, no deberías pedir comida chatarra hoy.")
    
def malestares():
    if malestar == "Sí":
        print("No sigas, no deberías pedir comida chatarra en esas condiciones.")
    else:
        print("Puedes ser gordo por hoy: pide tu antojo.")

dia_semana = input("Por favor indica qué día de la semana es hoy (no olvides las tildes y comienza con mayúscula): ")

if dia_semana == "Lunes":
    print("¿Es en serio? ¿Apenas lunes y ya pensando en tragar cosas poco saludables? La respuesta es no: no pidas ese antojo.")
elif dia_semana == "Martes" or "Miércoles" or "Jueves" or "Viernes" or "Sábado" or "Domingo":
    consumo_previo = input("¿Has consumido comida chatarra en los últimos 3 días? (Responde 'Sí' o 'No'): ")    
    consumo()
    malestar = input("¿Sientes, o has sentido en los últimos dos días, algún malestar asociado a posibles problemas digestivos? (Responde 'Sí' o 'No'): ")
    malestares()
else:
    print("Hiciste algo mal, inicia el programa nuevamente.")