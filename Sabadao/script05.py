lista = [1, 2, 3, 4]
# indexada
x = lista[0]

# lista 'nomeada' = dicionário
# estrutura: chave/valor
dicionario = {}
print('Dicionario vazio', dicionario)

dicionario = {
    1: 'Ozair',
    2: 'Pamela',
    3: 'Amanda',
    4: 'Aline',
    50: 'Luan'
}

print('Dicionario com chaves numericas', dicionario)

print('Chave 3:', dicionario [3])

existe_chave_5 = 5 in dicionario
if existe_chave_5:
    print("Chave 5:", dicionario)
else:
    print("Chave 5 nao existe")
#Tentar
