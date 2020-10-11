class Employee():
    def __init__(self, name, xing, money):
        self.names = xing + " " + name
        self.money = money
    
    def give_raise(self, add = 5000):
        self.money += add