products = {
    "laptop": {
        "name": "Laptop Pro 15",
        "price": 1299.99
    },
    "headphones": {
        "name": "Wireless Headphones",
        "price": 89.99
    },
    "keyboard": {
        "name": "Mechanical Keyboard",
        "price": 149.99
    },
    "mouse": {
        "name": "Ergonomic Mouse",
        "price": 49.99
    },
    "monitor": {
        "name": "4K UHD Monitor",
        "price": 599.99
    }
}

cart = []
bill_name = 'HERE YOUR BILL'
YOUR_ITEM ='YOUR ITEMS'
def design(): 
    print(f'{'='*35}')
    
def bill():
    total = 0
    for i in cart:
        if i in products:
            total += products[i]['price']
    return total

def bill_design():
    print(f'{'='*35}\n{bill_name.center(25)}\n{'='*35}')
    print(f"""{YOUR_ITEM.center(10,'*')}""")
    for i in cart:
        print('!',i)
    print('YOUR TOAL IS : ',bill())
    design()
    
def main():
    for keys in products:
        design()
        print()
        print(keys,':',products[keys]['name'],'-',products[keys]['price'],end='\n\n')
    while True :
        design()
        add_item = str(input('ETNER YOUR ITEMS (IF U DONE ENTER NO) : ')).strip().lower()
        if add_item == 'no':
                global ask_for_removing
                ask_for_removing = str(input('ANYTHING U WANT TO REMOVE? '))
                if ask_for_removing == 'no':
                    bill_design()
                    break
                if ask_for_removing in cart:
                    cart.remove(ask_for_removing)
                    print(f"'{ask_for_removing}' removed from cart.")
                else:
                    print(f"'{ask_for_removing}' not found in cart.")
                bill_design()
                break
        if add_item in products:
            cart.append(add_item)
        else:
            print('SORRU CURENTLY NOT AVALIABLE')
        print(cart)

main()