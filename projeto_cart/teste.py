# id produto, id usuario, preço, quantidade
carts = [['123', '1', 100.00, 2], ['456', '1', 899.00, 1]]

for item in carts:
    print(item)
    
## _________________________________________________
    
## Quero o item onde o produto for o tenis que o código é 123
    
new_lista = []
for item in carts:
    if item [0] == '123':
        new_lista.append(item)
        
print(new_lista[0])

#_________________________________________________

# forma 2:

new_lista = None
for item in carts:
    if item [0] == '123':
        new_lista = item
        
print(new_lista)

# _________________________________________________

# forma 3
# lista de compreensao
new_list = [item for item in carts if item[0] == '123']
print(new_list[0])

#___________________________________________






        


