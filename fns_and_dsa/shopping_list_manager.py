# Start with an empty shopping list
shopping_list = []

def display_menu():
    print("\nShopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        else:
            print("Item name cannot be empty.")
    
    elif choice == "2":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your shopping list.")
        else:
            print(f"'{item}' was not found in your shopping list.")
    
    elif choice == "3":
        if shopping_list:
            print("\nYour shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is currently empty.")
    
    elif choice == "4":
        print("Exiting the shopping list program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
