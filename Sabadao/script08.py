lista1 = [1, 2, 3, 4]

#Da lista1 incremetar os seus valores em 2
# e gerar uma lista2

# Forma 1
lista2 = []
for valor in lista1:
    novo_valor = valor + 2
    lista2.append(novo_valor)
    
print(0, lista1)
print(1, lista2)

# ____________________________________

#Forma 2
def somar_em2(valor):
    return valor + 2

objeto_mapeado = map(somar_em2, lista1)
lista2 = list(objeto_mapeado)
print (2, lista2)

# ___________________________________

#Forma 3
lista2 = [
    somar_em2(valor)
    for valor in lista1
]
print (3, lista2)


