import random

def generar_contrasena():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O']
    minusculas = ['a','b','c','d','e','f','g','h','i','j']
    simbolos = ['!','#','$','~','/']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros 

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres) #Con el metodo choice elijo un caracter al azar de toda mi lista de caracteres
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena) #A partir de esto puedo generar un string de mi lista original
    return contrasena 


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)

if __name__ == '__main__':
    run()