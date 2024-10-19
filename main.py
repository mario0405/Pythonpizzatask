from database import list_all_pizzas, find_pizzas_with_topping, find_pizza_by_name
# Importing functions from the database module

def main():
    # Main function that runs the menu
    while True:
        # Loop to display menu options continuously
        print("\nPizza Menu:")
        print("1. List all pizzas")
        print("2. Find pizzas with a specific topping")
        print("3. Select a pizza by name")
        print("4. Calculate pizza price with discount code")
        print("5. Exit")
        choice = input("Enter your choice: ").lower()
        # Get the user's choice and convert it to lowercase

        if choice == "1":
            # If user selects option 1, list all pizzas
            pizzas = list_all_pizzas()
            print("\nAvailable Pizzas:")
            for pizza in pizzas:
                # Print each pizza's details
                print(pizza)

        elif choice == "2":
            # If user selects option 2, search for pizzas with a specific topping
            topping = input("Enter the topping to search for: ").lower()
            pizzas = find_pizzas_with_topping(topping)
            if pizzas:
                # Print pizzas that have the topping
                print("\nPizzas with", topping, ":")
                for pizza in pizzas:
                    print(pizza)
            else:
                # If no pizzas have the topping, notify the user
                print("No pizzas found with that topping.")

        elif choice == "3":
            # If user selects option 3, search for a pizza by its name
            name = input("Enter the name of the pizza: ").lower()
            pizza = find_pizza_by_name(name)
            if pizza:
                # Print details of the selected pizza
                print("\nSelected Pizza Details:")
                print(pizza.get_details())
            else:
                # If pizza isn't found, notify the user
                print("Pizza not found.")

        elif choice == "4":
            # If user selects option 4, calculate pizza price with discount
            name = input("Enter the name of the pizza: ").lower()
            pizza = find_pizza_by_name(name)
            if pizza:
                discount_code = input("Enter discount code (or press Enter to skip): ")
                if discount_code == "PIZZA10":
                    # Apply 10% discount if the code is correct
                    discounted_price = pizza.price * 0.9
                    print("Discounted price: $" + str(round(discounted_price, 2)))
                else:
                    # Show regular price if no discount code
                    print("Price: $" + str(round(pizza.price, 2)))
            else:
                # If pizza isn't found, notify the user
                print("Pizza not found.")

        elif choice == "5":
            # If user selects option 5, exit the program
            print("Exiting...")
            break
        else:
            # If the input is invalid, ask the user to try again
            print("Please try again. Your choice is invalid.")

if __name__ == "__main__":
    main()
    # Run the main function if the script is executed directly
