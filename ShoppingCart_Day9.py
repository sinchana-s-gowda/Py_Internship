class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        self.cart[item] = quantity

    def display_cart(self):
        print(self.cart)

    def update_item(self, item, new_quantity):
        if item in self.cart:
            self.cart[item] = new_quantity

    def delete_item(self, item):
        if item in self.cart:
            del self.cart[item]


cart = ShoppingCart()
cart.add_item("XYZ", 2)
cart.add_item("ABC", 1)
cart.display_cart()
cart.update_item("XYZ", 5)
cart.delete_item("ABC")
cart.display_cart()