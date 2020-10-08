from restaurant import Restaurant

class NewRestaurant(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['ad', 'adf', 'aewfasd']

    def printf(self):
        for flavor in self.flavors:
            print(flavor)


ice = NewRestaurant('12', 'a')
ice.printf()