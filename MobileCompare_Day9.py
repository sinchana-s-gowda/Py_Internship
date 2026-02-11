class MobileComparison:
    def __init__(self):
        self.mobiles = {}

    def add_mobile(self, name, price):
        self.mobiles[name] = price

    def display_mobiles(self):
        print(self.mobiles)

    def update_mobile(self, name, new_price):
        if name in self.mobiles:
            self.mobiles[name] = new_price

    def delete_mobile(self, name):
        if name in self.mobiles:
            del self.mobiles[name]


mobile = MobileComparison()
mobile.add_mobile("XYZ", 20000)
mobile.add_mobile("ABC", 15000)
mobile.display_mobiles()
mobile.update_mobile("XYZ", 22000)
mobile.delete_mobile("ABC")
mobile.display_mobiles()