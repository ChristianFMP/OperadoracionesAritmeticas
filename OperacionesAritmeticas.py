# Programa Principal
# Menu de opciones
def MenuOpciones():
    print("HOLA GRACIAS POR USAR NUESTRO SOFTWARE")
    print("MARQUE LA OPCIÓN QUE DESEA HACER")
    print("Presione 1 para sumar")
    print("Presione 2 para restar")
    print("Presione 3 para multiplicar")
    print("Presione 4 para dividir")
    print("Presione 5 para salir")
    opcion = int(input("Por favor ingrese su opción: "))
    while((opcion < 1) or (opcion > 5 )):
        print("Por favor ingrese una opción válida del menú")
        opcion = int(input("Ingrese nuevamente su opción: "))
    print("El resultado de su operación es: ")
    
MenuOpciones()