class Pessoa:
    def __init__(self, cpf, nome, idade, fumante):
        self.cpf = cpf 
        self.nome = nome 
        self.idade = idade 
        self.fumante = fumante

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade, fumante, cidade):
        self.cidade = cidade
        
        super().__init__(cpf, nome, idade, fumante) 
        
    def dados(self):
        if self.fumante == "F":
            return f'{self.nome}, CPF: {self.cpf}, mora em {self.cidade}, tem {self.idade} anos e é fumante'
        
        if self.fumante == "N":
            return f'{self.nome}, CPF: {self.cpf}, mora em {self.cidade}, tem {self.idade} anos e não é fumante'
        
pessoa1 = PessoaFisica('111.222.333-44', 'Ana', '30', 'F', 'Florianópolis')
pessoa2 = PessoaFisica('222.333.444-55', 'Beatriz', '25', 'N', 'São Paulo')

print(pessoa1.dados())
print(pessoa2.dados())    
    