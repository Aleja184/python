#Programa para filtrar datos usando high order functions
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    all_python_devs = list(filter(lambda workers: workers['language'] == 'python',DATA)) #Devuelve la lista con los trabajadores que usan python
    all_python_devs = list(map(lambda workers: workers['name'],all_python_devs)) #Devuelve solo los nombres de los trabajadores que usan python
    
    all_platzi_workers = list(filter(lambda workers: workers['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda workers: workers['name'],all_platzi_workers))

    adults = [worker['name'] for worker in DATA if worker['age']>18] #Devuelve el nombre de los trabajadores mayores de 18. Uso de list comprehensions

    old = [worker | {'old': worker['age']>70} for worker in DATA] #Une un nuevo diccionario al anterior agregando el valor booleana dependiendo de la edad del trabajador.
    
    for worker in old:
        print(worker)

if __name__ =='__main__':
    run()