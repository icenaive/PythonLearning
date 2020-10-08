class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def des_res(self):
        print("name is: %s, cuisine is: %s" % (self.name, self.cuisine_type))
    
    def open_res(self):
        print("openning")
    
    def set_num(self, num):
        self.number_served = num
    
    def incre(self, num):
        self.number_served += num