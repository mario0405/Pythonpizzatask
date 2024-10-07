from pizza import Pizza

pizzas = [
    Pizza("Margherita", ["tomato", "mozzarella"], 8.50),
    Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"], 9.50),
    Pizza("Hawaiian", ["ham", "pineapple"], 10.00),
    Pizza("Veggie", ["tomato", "mozzarella", "peppers", "onions"], 9.00)
]

def list_all_pizzas():
    return [pizza.get_details() for pizza in pizzas]

# Füge das Argument 'topping' hinzu
def find_pizzas_with_topping(topping):
    return [pizza.get_details() for pizza in pizzas if pizza.has_topping(topping)]

# Füge das Argument 'name' hinzu
def find_pizza_by_name(name):
    for pizza in pizzas:
        if pizza.name.lower() == name.lower():
            return pizza
    return None
