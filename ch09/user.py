class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.jianjie = {'2':'12'}
        self.login = 0

    def des_user(self):
        print(self.first_name, self.last_name, self.jianjie)
    
    def greet(self):
        print("hello %s" % self.last_name.title(), self.login)
    
    def incre(self):
        self.login += 1
    
    def reset(self):
        self.login = 0