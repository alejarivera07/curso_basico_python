# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("¡Estoy aprendiendo a usar funciones!")


# imprimir_mensaje()
def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion = int(input("Elije una opión (1,2,3): "))
if opcion == 1:
   conversacion('Elejiste la opción 1')
elif opcion == 2:
    conversacion('Elejiste la opción 2')
elif opcion == 3:
    conversacion('Elejiste la opción 3')
else:
    print("Escribe la opción correcta") 