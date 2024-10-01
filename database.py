from pizza import Pizza

pizzas = [                                   #4 Bsp Pizzen mit deren Toppings und Preis l alles in einer sogenannten mock database
    Pizza("Margherita", ["tomato", "mozzarella"], 8.50),
    Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"], 9.50),
    Pizza("Hawaiian", ["ham", "pineapple"], 10.00),
    Pizza("Veggie", ["tomato", "mozzarella", "peppers", "onions"], 9.00)
]

def list_all_pizzas():
    return [pizza.get_details() for pizza in pizzas]

def find_pizzas_with_topping():
    return [pizza.get_details() for pizza in pizzas if pizza.has_topping(topping)]

def find_pizza_by_name():
    for pizza in pizzas:
        if pizza.name.lower() == name.lower():
            return pizza
    return None
