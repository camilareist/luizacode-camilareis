minha_string = "O rato roeu a roupa do rei de Roma"

# método find retorna qual o indice
# dessa posição da palavra
busca = minha_string.find("rei")

print(busca)

# para imprimir da busca até o final
print(minha_string[busca:])

# ________________________________________

# metodo replace substitui a string por outra
minha_string = minha_string.replace("o rei","a rainha")
print(minha_string)
