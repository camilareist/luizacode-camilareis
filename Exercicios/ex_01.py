class Pessoa:
    def __init__(self, cpf, nome, idade, fumante):
        self.cpf = cpf 
        self.nome = nome 
        self.idade = idade 
        self.fumante = fumante
    
    def fuma(self):
        if self.fumante == "F":
            return f'{self.nome} de CPF {self.cpf} possui {self.idade} anos de idade e é fumante'
        
        if self.fumante == "N":
            return f'{self.nome} de CPF {self.cpf} possui {self.idade} anos de idade e não é fumante'
    
pessoa1 = Pessoa("123.456.789-10", "Aline", "20", "F").fuma()
pessoa2 = Pessoa("000.000.000-00", "Bruna", "25", "F").fuma()
pessoa3 = Pessoa("777.555.998-91", "Julia", "23", "N").fuma()

print(pessoa1)
print(pessoa2)
print(pessoa3)


    
    
    