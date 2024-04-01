import random

def read():
    palabra = ""
    #abre archivo y lo maneja como f
    with open("Intermedio/Proyecto/data.txt","r",encoding="utf8") as f:
        #lee todas las lineas del archivo
        iterables = f.readlines()
        #elige una aleatoriamente del archivo
        palabra = random.choice(iterables).strip()
        # print(iterables)
        # print(palabra)
    return palabra 
    # retorna la variable palabra

def opcion1():
    Palabra_aleatoria=read()
    return Palabra_aleatoria




