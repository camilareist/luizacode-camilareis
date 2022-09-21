import logging

logging.basicConfig(level='INFO', filename='logging_user.log')

users = []

def users_validate(name):
    for user in users:
        if user['name'] == name:
            raise TypeError('Já existe um usuário cadastrado com esse nome')

def age_validate(age):
    if age < 18 or age > 100:
        raise TypeError('Usuário deve ser maior de 18 anos e menor de 100 anos')

def name_validate(name):
    if len(name) < 10:
        raise TypeError('Nome do usuário deve conter mais de 10 caracteres')
              
def user_add():
    try:
        name = input("Digite o nome do usuário: ")
        name_validate(name)
        users_validate(name)
        age = int(input("Digite a idade do usuário: "))
        age_validate(age)
    except ValueError:
        print('Erro nos tipos de dados digitados')
        logging.error('Erro nos dados digitados')
        return
    except TypeError as error:
        print(error)
        logging.error(error)
        return
           
    users.append({"name": name, "age": age})
    
    print("\nUsuário cadastrado com sucesso!")
    
def users_list():
    print("\n")
    for user in users:
        print("{} - {} anos".format(user["name"], user["age"]))

while True:
    option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
    
    if option == 1:
        user_add()
    elif option == 2:
        users_list()
    elif option == 3:
        exit()
    else:
        print("Opção inválida!")
        


