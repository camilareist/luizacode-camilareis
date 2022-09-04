cart = [['1', '123', 899.00, 1], ['1','456', 549.00, 1], ['1','789', 100.00, 1]]
print(cart)

def remove_item_id():
    for item in cart:
        if item[1] == '123':
            cart.pop(item)
            
remove_item_id()        
print(cart)