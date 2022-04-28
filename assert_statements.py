#Programa para devolver los divisores de un número
def divisors(num): #Función que pide como parametro el número y devuelve el divisor.
    divisors = [i for i in range(1,num+1) if num%i==0]
    print(divisors)
    

def run():
    num = int(input('Ingresa un número: '))
    #assert num.isnumeric(), 'Debes ingresar un número' #El método isnumeric() devuelve un valor booleano si la variable es un número o no.
    assert num > 0, 'Debes ingresar un número positivo'
    divisors(int(num))

if __name__ == '__main__':
    run()