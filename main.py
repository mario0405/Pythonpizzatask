from database import list_all_pizzas, find_pizzas_with_topping, find_pizza_by_name

def main():
    while True:
        print("\nPizza Menu:")
        print("1. List all pizzas")
        print("2. Find pizzas with a specific topping")
        print("3. Select a pizza by name")
        print("4. Calculate pizza price with discount code")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":  # Alle Pizzas auflisten
            pizzas = list_all_pizzas()  # Funktionsname auf "list_all_pizzas" geändert
            print("\nAvailable Pizzas:")
            for pizza in pizzas:
                print(pizza)

        elif choice == "2":  # Pizzen mit einem spezifischen Topping
            topping = input("Enter the topping to search for: ")
            pizzas = find_pizzas_with_topping(topping)  # Funktionsname auf "find_pizzas_with_topping" geändert
            if pizzas:
                print("\nPizzas with", topping, ":")
                for pizza in pizzas:
                    print(pizza)
            else:
                print("No pizzas found with that topping.")

        elif choice == "3":  # Pizzen mit einem spezifischen Namen
            name = input("Enter the name of the pizza: ")
            pizza = find_pizza_by_name(name)  # Funktionsname auf "find_pizza_by_name" geändert
            if pizza:
                print("\nSelected Pizza Details:")
                print(pizza.get_details())
            else:
                print("Pizza not found.")

        elif choice == "4":  # Preis mit Rabatt berechnen
            name = input("Enter the name of the pizza: ")
            pizza = find_pizza_by_name(name)  # Auch hier den Funktionsnamen angepasst
            if pizza:
                discount_code = input("Enter discount code (or press Enter to skip): ")
                if discount_code == "PIZZA10":
                    discounted_price = pizza.price * 0.9  # 10% Rabatt
                    print("Discounted price: $" + str(round(discounted_price, 2)))
                else:
                    print("Price: $" + str(round(pizza.price, 2)))
            else:
                print("Pizza not found.")

        elif choice == "5":  # Programm verlassen
            print("Exiting...")
            break
        else:
            print("Please try again. Your choice is invalid.")


if __name__ == "__main__":
    main()
