class Pizza:
  def __init__(self, name, toppings, price):
    self.name = name
    self.toppings = toppings
    self.price = price

  def get_details(self):
    return self.name + ": " + ", ".join(self.toppings) + " - $" + str(round(self.price, 2)) 
    #noch vereinfachen...
  
  def has_topping(self, topping):
    return topping in self.toppings
