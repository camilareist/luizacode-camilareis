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

#Tentar pegar uma chave sem precisar testa
etiqueta = 5
valor_chave_5 = dicionario.get(etiqueta)
print("Valor com chave 5:", valor_chave_5)

#pegadinha
dicionario = {
    5: None
}
print ('Engana 1:', dicionario.get(5))
print('Confirmando a chave?', 5 in dicionario)
