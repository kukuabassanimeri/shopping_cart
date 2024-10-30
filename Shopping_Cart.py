#Write python program to do shopping cart
class ShoppingCart:
    def __init__(self, cart_name):
        self.cart_name = cart_name
        self.items = []
    
    #Method that diplays cart details
    def display_cart_details(self):
        print(f"Cart Name: {self.cart_name}")
    
    #Method that add items to the cart    
    def add_item(self, item_name, quantity, item_price):
        item = { 'name': item_name, 'quantity': quantity, 'price': item_price, }
        self.items.append(item)
        print(f"Added {quantity}  {item_name} (s) at ${item_price} each to the cart.")
    
    #Method that view items from the cart
    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        else:
            print("Items in the cart:")
            for item in self.items:
                print(f"{item['quantity']}  {item['name']} each at {item['price']}")
            print(f"Total cart value: ${self.total_price()}")
    
    #Method that calculate the total price of item in the cart
    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    #Method that remove items from the cart
    def remove_item(self, item_name, quantity_to_remove):
        for item in self.items:
            if item['name'] == item_name:
                if item['quantity'] > quantity_to_remove:
                    item['quantity'] -= quantity_to_remove
                    print(f"Removed {quantity_to_remove} {item_name}(s) from the cart. Remaining: {item['quantity']}")
                elif item['quantity'] == quantity_to_remove:
                    self.items.remove(item)
                    print(f"Removed all {item_name}(s) from the cart.")
                else:
                    print(f"Cannot remove {quantity_to_remove} {item_name}(s); only {item['quantity']} available.")
                return
        print(f"{item_name} not found in the cart.")
    
    #Method that update item name from the cart
    def update_item(self, old_item_name, new_item_name):
        for item in self.items:
            if item['name'] == old_item_name:
                item['name'] = new_item_name
                print(f"Name of {old_item_name} has been updated to {new_item_name}.")
                return
        print(f"{old_item_name} not found in the cart.")
        
        
    #Method that update price of items in the cart
    def update_price(self, item_name, new_price):
        for item in self.items:
            if item['name'] == item_name:
                item['price'] = new_price
                print(f"Price of {item_name} has been updated to ${new_price}.")
                return
        print(f"{item_name} not found in the cart.")
        
        
    #Method that update quantity of items in the cart
    def update_quantity(self, item_name, new_quantity):
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] = new_quantity
                print(f"Quantity of {item_name} has been updated to {new_quantity}.")
                return
        print(f"{item_name} not found in the cart.")

#child class
class Yaka_shopping_cart(ShoppingCart):
    def __init__(self, cart_name):
        super().__init__(cart_name)
        
    def yaka_add_item(self):
        item_name = input("Enter the name of the item to add to the card: ")
        quantity = int(input("Enter the quantity of items to add to the card: "))
        price = float(input("Enter the price per an item: "))
        self.add_item(item_name, quantity, price)
        
        