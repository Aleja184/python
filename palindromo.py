#Programa que verifica si una palabra es un palindromo o no
def palindromo(palabra): #Se define la función palindromo que recibe como parametro una palabra
    palabra = palabra.replace(' ','')#Se quitan los espacios de la palabra 
    palabra = palabra.lower()#Se pone en minuscula
    palabra_invertida = palabra[::-1] #Se le asigna a la variable palabra_invertida la variable palabra
    if palabra == palabra_invertida:#Se compara palabra original con palabra_invertida
        return True
    else:
        return False

def run(): #Función donde se le pide al usuario ingresar la palabra 
    palabra = input('Ingrese una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__': 
    run()