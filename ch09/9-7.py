from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['ad', 'adf', 'adfsdf']
    
    def show(self):
        print(self.privileges)

class NewUser(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()



admin = NewUser('awefad', 'adfasdf')
admin.privileges.show()