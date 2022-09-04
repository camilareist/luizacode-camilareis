"""
Dicionários são listas de associações
compostas por:
- uma chave;
- um valor correspondente.

dicionario = {'CHAVE':'valor'}
    """
    
meu_dicionario = {"A": "AMEIXA", "B": "BOLA", "C":"CACHORRO"}
# dicionario não tem indice

# Chamar pela chave
print(meu_dicionario["A"])

for chave in meu_dicionario:
    print(chave+"-"+meu_dicionario[chave])
    
# função items, retorna todos os items do dicionario
# como uma tupla
for i in meu_dicionario.items():
    print(i)
    
# função values, retorna só os valores
for i in meu_dicionario.values():
    print(i)
    
# função keys, retorna só as chaves
for i in meu_dicionario.keys():
    print(i)

    