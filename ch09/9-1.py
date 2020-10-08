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

res1 = Restaurant("123", "shaokao")
print(res1.number_served)
res1.number_served = 100
print(res1.number_served)
res1.set_num(1000)
print(res1.number_served)
res1.incre(100)
print(res1.number_served)

# res2 = Restaurant("1233", "3")
# res3 = Restaurant("23", "23")

# #print("res de name is: %s, res de type is %s" % (res.name, res.cuisine_type))
# res1.des_res()
# res2.des_res()
# res3.des_res()
#res.open_res()