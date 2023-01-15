from user import User
class Admin(User):
    def __init__(self,first_name,last_name,age,city,phone):
	    super().__init__(first_name,last_name,age,city,phone)
	    self.privileges = Privileges()



class Privileges():
    def __init__(self):
	    self.privileges = ['permission del', 'permission enter', 'full_permission', 'permission denide']
    def show_privileges(self):
	    print("\nList privilages for Admin: ")
	    print(self.privileges)
