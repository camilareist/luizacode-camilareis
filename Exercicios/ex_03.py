class Pessoa:
    def __init__(self, cpf):
        self.cpf = cpf
        
    def tipo_pessoa(self):
        return f'Esta é uma pessoa física, de CPF {self.cpf}'
    
class Pessoajuridica(Pessoa):
    def __init__(self, cpf, cnpj):
        self.cnpj = cnpj
        
        super().__init__(cpf)
        
    def tipo_pessoa(self):
        return f'Esta é uma pessoa juridica de CNPJ {self.cnpj}'
      
pessoa_fisica = Pessoa('111.222.333-44')
pessoa_juridica = Pessoajuridica('xxxx', '11.222.333/0000-11')

print(pessoa_fisica.tipo_pessoa())
print(pessoa_juridica.tipo_pessoa())

        
        
