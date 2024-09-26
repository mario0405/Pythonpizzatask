from x import y

def main():
    while True:
        print("\nPizza Menu:")
        print("1. List all pizzas")
        print("2. Find pizzas with a specific topping")
        print("3. Select a pizza by name")
        print("4. Calculate pizza price with discount code")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1": #Alle Pizzas auflisten
            xy

        elif choice == "2": #Pizzen mit xy Topping
            topping = input("Enter the topping to search for: ")
        
        elif choice == "3": #Pizzen mit xy Namen
            name = input("Enter the name of the pizza: ")

        elif choice == "4": #Preis mit Rabatt berechnen
            name = input("Enter the name of the pizza: ")

        elif choice == "5": #Programm verlassen
            print("Exiting...")
            break
        else: 
            print("please try again. We couldnt find your choice")
