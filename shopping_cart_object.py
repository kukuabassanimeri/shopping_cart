from Shopping_Cart import Yaka_shopping_cart

def main():
    cart = Yaka_shopping_cart("Yaka E-commerce Shopping Cart")
    cart.display_cart_details()
    
    while True:
        print("\nSelect an option:")
        print("1. Add an item to the cart")
        print("2. View items in the cart")
        print("3. Remove an item from the cart")
        print("4. Update item name in the cart")
        print("5. Update item price in the cart")
        print("6. Update item quantity in the cart")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            cart.yaka_add_item()
        
        elif choice == '2':
            cart.view_cart()
        
        elif choice == '3':
            item_name = input("Enter the name of the item to remove: ")
            quantity_to_remove = int(input("Enter the quantity to remove: "))
            cart.remove_item(item_name, quantity_to_remove)
        
        elif choice == '4':
            old_name = input("Enter the current name of the item: ")
            new_name = input("Enter the new name of the item: ")
            cart.update_item(old_name, new_name)
        
        elif choice == '5':
            item_name = input("Enter the name of the item to update the price: ")
            new_price = float(input("Enter the new price: "))
            cart.update_price(item_name, new_price)
        
        elif choice == '6':
            item_name = input("Enter the name of the item to update the quantity: ")
            new_quantity = int(input("Enter the new quantity: "))
            cart.update_quantity(item_name, new_quantity)
        
        elif choice == '7':
            print("Exiting the program. Thank you for shopping with us!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the main program
if __name__ == "__main__":
    main()