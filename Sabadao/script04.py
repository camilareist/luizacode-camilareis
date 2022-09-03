#Somar todos os elementos pares da lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for valor in lista:
    #Somar somente para os casos em que os 
    # números são pares
    if valor % 2 == 0:
        soma = soma + valor 
#fimdofor

print('Resultado', soma)

#------------------------------------------------

soma = 0
#Invertido
for valor in lista:
      if valor % 2 != 0:
          #continue para o prox se o n é impar
          continue
      #else: 
      soma = soma + valor
#fimdofor

print("resultado invertido", soma)



