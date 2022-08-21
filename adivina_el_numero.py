import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elije un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
            numero_elegido = int(input('Elije otro número: '))
        else:
            print('Busca un número menor')
            ## esto para que vuelva a elegir un número 
            numero_elegido = int(input('Elije otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()