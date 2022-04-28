#Juego del ahorcado
from concurrent.futures.process import _ThreadWakeup
from distutils.log import error
from multiprocessing.sharedctypes import Value
import os
from random import randint

def start(): #Función para limpiar la pantalla
    os.system('cls')
def game():
    with open("./archivos./data.txt","r",encoding="utf-8") as f:#lectura archivo
        words = [word for word in f]
    number = randint(1,171)
    choose_word = words[number]
    word = ['_' for i in range(len(choose_word)-1)]#variable que contiene los espacios para cada letra de la palabra
    aciertos = int(0)
    for i in range(0,10):#10 oportunidades para acertar la palabra
        if aciertos >= len(choose_word)-1:
            break
        letra = input('Digite una letra en minúscula: ')
        try: 
            if letra == '' or len(letra)>=2:#Comprobación de que se introduzca una letra
                raise ValueError('Debe ingresar una letra')
            for j in range(0, len(choose_word)-1):#Busqueda de la letra en la palabra
                if letra == choose_word[j]:
                    aciertos = aciertos + 1
                    word[j] = letra
                    os.system('cls')
                    print(' '.join(word))
                else:
                    os.system('cls')
                    print(' '.join(word))
        except ValueError as ve:
            print(ve)
            return False
    if aciertos == len(choose_word)-1:#Se comprueba si se ganó o se perdió
        print('Felicidades')
    else:
        print('Suerte a la próxima')
                
def run():
    start()
    game()

if __name__=='__main__':
    run()
