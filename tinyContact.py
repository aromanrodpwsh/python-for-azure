names=[]
addresses=[]
telephone=[]

def new_contact():
    print('Create new contact: ')
    names.append(input('Enter Contact name: '))
    addresses.append(input('Enter contact address: '))
    telephone.append(input('Enter contact telephone: '))


def find_contact():
    name_position=0
    print('Find Contact')
    search_name=input('Enter contact name: ')
    for name in names:
        if name==search_name:
            break
        name_position=name_position+1

    if name_position < len(names):
        print('Name: ', names[name_position])
        print('Adress: ', addresses[name_position])
        print('Telephone: ', telephone[name_position])

def welcome():
    print('''Bienvenida a la libreta de contactos
          Selecciona la opcion deseada:
          1. Crear contacto
          2. Buscar Contacto
          3. salir''')
    selection=input('seleccione una opcion: ')
    return selection

option='0'
while option != '3':
    option=welcome()
    if option == '1':
        new_contact()
        option='1'
    elif option == '2':
        find_contact()
        option='2'
    elif option == '3':
        option='3'
    else:
        print('Esta opcion no es valida')

print('Gracias por usar el programa')