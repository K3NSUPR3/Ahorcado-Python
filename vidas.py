def juego_con_vidas(letra, palabra_oculta, intentos, vidas):
    """
    """
    if letra in intentos:
        print("Ya ingresaste ese carácter! Perdiste una vida.")
        vidas -= 1
    elif letra in palabra_oculta:
        print("Bien hecho, sigue jugando.")
    else:
        print("Esa letra no está en la palabra. Perdiste una vida.")
        vidas -= 1

    intentos.append(letra)

    if vidas == 0:
        print("Juego terminado. No te quedan vidas ")
    else:
        print(f"Vidas restantes: {vidas}")

    return vidas


if __name__ == "__main__":
   print(juego_con_vidas)
    
        
