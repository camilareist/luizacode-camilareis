#Somar todos os elementos da lista
#Com um laço de repetição

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#blocos de instrução: indentação
#laço de repetição

soma = 0
#para cada valor na lista
for valor in lista:
    #inicio do bloco/conj. de instruções
    #a serem executadas pelo laço
    soma = soma + valor
#fim do for

print('Resultado', soma)

soma = sum(lista)
print(' Resultado por sum():', soma)

