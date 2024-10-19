class Pizza:
    # Defines the Pizza class
    def __init__(self, name, toppings, price):
        # Initialize pizza with a name, toppings, and price
        self.name = name
        self.toppings = toppings
        self.price = price

    def get_details(self):
        # Returns the pizza's details as a string (name, toppings, and price)
        return self.name + ": " + ", ".join(self.toppings) + " - $" + str(round(self.price, 2))

    def has_topping(self, topping):
        # Checks if the pizza has the specified topping
        return topping in self.toppings
