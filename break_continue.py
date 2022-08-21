def run():
    for contador in range(1000):
        # si esta condici+on no se cumple me salto esta 
            # vuelta del ciclo y lo que esta debajo de la 
            # palabra continue no se va a ejecutar
        # ----------- EJEMPLO --------------------------
        # if contador % 2 != 0: 
        #     continue
        # print(contador)
        # ---------- EJEMPLO --------------------------
        # for i in range(10000):
        #     print(i)
        #     if i == 5678:
        #         break
        # ---------- EJEMPLO --------------------------
        texto = input('escribe un texto: ')
        for letra in texto:
            if letra == 'o':
                break  ##cortar con el ciclo
            print(letra)


if __name__ == '__main__':
    run()