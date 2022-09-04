a = "Diego"
b = "Mariano"

concatenar = a + " " + b

# concatenando strings
print(concatenar)

# função para transformar string em minúsculo
print(concatenar.lower())

#função para transformar string em maiusculo
print(concatenar.upper())

# variavel ira adotar o valor em maiusculo
concatenar = concatenar.upper()

# _____________________________________________

concatenar = a + " " + b + "\n"
concatenar2 = a + " " + b + "\n"

# \n utilizado para pular linha após resultado da string

# Função strip remove caracteres especiais ou espaços 
# no fim da string
print(concatenar.strip())
print(concatenar2)

# ___________________________________________________

minha_string = "O rato roeu a roupa do rei de Roma"

# converte a string em lista separando por espaços
minha_lista = minha_string.split()
print(minha_lista)

# pode escolher a quebra por letras, no exemplo abaixo
# quebramos na letra R
minha_lista = minha_string.split("r")
print(minha_lista)





