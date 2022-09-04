import random

# Buscar numero aleatório, de 0 até 10
numero = random.randint(0,10)
print(numero)

# ______________________________________

# forçar o python a trazer sempre 
# o mesmo número usando seed

random.seed(1)
numero = random.randint(0,10)
print(numero)

# ____________________________________

# escolhe algum item aleatório da lista
lista = [6, 45, 9]
numero = random.choice(lista)
print(numero)