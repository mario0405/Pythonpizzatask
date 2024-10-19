from pizza import Pizza
# Import the Pizza class from the pizza module

pizzas = [
    # Create a list of Pizza objects with their names, toppings, and prices
    Pizza("Margherita", ["tomato", "mozzarella"], 8.50),
    Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"], 9.50),
    Pizza("Hawaiian", ["ham", "pineapple"], 10.00),
    Pizza("Veggie", ["tomato", "mozzarella", "peppers", "onions"], 9.00)
]

def list_all_pizzas():
    # Returns a list of all pizza details
    return [pizza.get_details() for pizza in pizzas]

def find_pizzas_with_topping(topping):
    # Returns pizzas that have the specified topping
    return [pizza.get_details() for pizza in pizzas if pizza.has_topping(topping)]

def find_pizza_by_name(name):
    # Finds a pizza by its name
    for pizza in pizzas:
        if pizza.name.lower() == name.lower():
            return pizza
    return None
    # Returns None if no pizza is found with the given name
