

def make_pizzaplus1(size,*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " +str(size) + "-inch pizza with the followings:")
    for topping in toppings:
        print("-" + topping)
