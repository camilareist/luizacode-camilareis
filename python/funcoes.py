"""
Funções em python são definidas pela 
palavra reservada def

definição: 
def NOME(PARÂMETROS)
    COMANDOS
    
Chamada:
NOME(ARGUMENTOS)    
    """
    
def soma(x,y):
    print(x+y)

soma(2,3)    

# ______________________________________

def soma(x,y):
    return x + y

s = soma(2,3)
print(s)

