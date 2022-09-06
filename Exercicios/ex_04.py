class Professor:
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        
    def __buscasalario(self):
        return f'O salário do professor {self.nome} é de {self.salario}'
        
    def userconsulta(self, cargo):
        if cargo == 'Diretor':
            return self.__buscasalario()
            
professor1 = Professor('João', '33', 'Professor', 'R$ 5000.00').userconsulta('Diretor')
# professor2 = Professor('Fabio', '40', 'Professor', 'R$ 7000.00').__buscasalario()

print(professor1)
# print(professor2)
        