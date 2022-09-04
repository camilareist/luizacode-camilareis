minha_lista = ['abacaxi', 'melancia', 'abacate']

# adicionar item no fim da lista
minha_lista.append("limão")

print(minha_lista)

# __________________________________

# Verifica se existe elemento na lista

lista = [1, 2, 3, 4, 5]

if 7 in lista:
    print("7 está na lista")
else:
    print("7 não está na lista")
    
# _______________________________________

# Remover item da lista
# do item 2 a diante
del minha_lista[2:]
print(minha_lista)

# para apagar toda lista
del minha_lista[:]
print(minha_lista)