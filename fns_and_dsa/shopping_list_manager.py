def display_menu():
    """Prints the menu options for the shopping list manager."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("-----------------------------\n")

def main():
    # Initialize the empty list to store shopping items
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # 1. Add Item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the user didn't enter an empty string
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")
            else:
                print("Item cannot be empty.")
            
        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The shopping list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            
            try:
                # Attempt to remove the item. Python's list.remove() handles the search.
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                # Handle the case where the item is not found in the list
                print(f"Error: '{item_to_remove}' was not found in the list.")
            
        elif choice == '3':
            # 3. View List
            print("\n--- Current Shopping List ---")
            if shopping_list:
                # Use a for loop to print each item clearly
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty!")
            print("-----------------------------\n")
            
        elif choice == '4':
            # 4. Exit
            print("Goodbye! Happy shopping!")
            break
            
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
