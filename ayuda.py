import os 
import menu
import vidas
import leerDatos
#importa las funciones del archivo

#se importa la funcion imprimir 
menu.impresion()
vidasJ=6
intentos=[]
palabra=[]

try:
    seleccion = int(input(" Selecciona una Opcion "))
    if seleccion==1:
        palabra=leerDatos.opcion1()
    elif seleccion==2:
        #forma manual
        palabra = input('2 Ingresa una palabra para adivinar Versus: ')
    elif seleccion==3:
        raise SystemExit
    else:
        print("404 No se ha encontrado")
        Mala=input("escriba 0 para regresar ")
        if Mala==0:
            menu.impresion()
        else:
            SystemExit
except ValueError:
    print("opcion debe ser en numero ")

#palabra_list =["a","b","c","d","e","f","g","h","i"]
palabra_list =["_"]*len(palabra) # mas de 4
# for i in range(len(palabra_list)):
#     palabra_list[i] = str()

while True:
    
    #limpia la consola con el comando
    os.system('cls') # limpiar
    print(" Adivina la palabra ")
    #concatena una palabra elegida
    print("".join(palabra_list))
    #El usuario ingresa un caracter
    try:
        while vidasJ >0:
            letra=input(("Ingresa una letra para adivinar que  palabra es: "))
            resultado=vidas.juego_con_vidas(letra,palabra,intentos,vidasJ)
            vidasJ=resultado

            if "_" not in palabra:
                print("Felicidades loc@ ")
                break
        
        if(vidasJ <= 0):
            print("Perdiste vida final")
            print("La palabra era: "+ palabra)
            menu.muerte()

    except EOFError as e:
        print("Error no ingresaste nada",e)
    finally:
        print(" _____ ")    

    if len(letra)>1:
        for i in range(len(palabra_list)):
            if letra == palabra[i]:
                palabra_list[i] = letra
    else:
        for i in range(len(palabra_list)):
            if letra == palabra[i]:
                palabra_list[i] = letra
    if "".join(palabra_list)==palabra:
        print(" Ganaste ")
        print("La palabra es: "+ palabra)
        break
print("Termino la Ejecucion ")