cart = []

id_user = input("Insira o id do usuário:")
id_product = input("Insira o id do produto:")
price_product = float(input("Insira o preço do produto:"))
quantity_product = int(input("Insira a quantidade de produto:"))

item = [id_user, id_product, price_product, quantity_product]

# Adicionar itens carrinho
def add_item_cart():
    cart.append(item)

add_item_cart()

def get_all_itens_cart():
    print(cart)

get_all_itens_cart()

def get_item_cart_by_product(id_product):
    new_list = [item for item in cart if item[1] == id_product]
    print(new_list[0])
     
get_item_cart_by_product(id_product)
