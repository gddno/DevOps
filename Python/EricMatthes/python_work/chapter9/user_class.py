class User():
    def __init__(self,first_name,last_name,age,city,phone):
	    self.first = first_name
	    self.last = last_name
	    self.age = age
	    self.phone = phone
	    self.city = city
	    self.login_attempts=0
    def describe_user(self):
	    print("\nInformation about user "+ self.last.title()+" " + self.first.title() + ": ")
	    print("\n-First name: " + self.first.title())
	    print("\n-Last name: " + self.last.title())
	    print("\n-Phone: " + str(self.phone))
	    print("\n-City: " + self.first.title())
	    print("\n-Age: " + str(self.age))
	    print("\n-Login attempts: "+str(self.login_attempts))
    def greet_user(self):
	    print("\nWe greet user " + self.first.title() + "!!!!")
    
    def increment_login_attempts(self):
	    self.login_attempts += 1
    
    def reset_login_attempts(self):
	    self.login_attempts = 0



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




i = User('dima','zhuravlev',26,'St.Pe',89183288814)
van = User('vanya','trushin',23,'vladivostok',89183288815)
sanya = User('sanay','rybacode',23,'yaroslavl',89124588890)
admin = Admin('admin','admin',34,'adminovsk',89003211235)
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.describe_user()
i.reset_login_attempts()
i.describe_user()
i.greet_user()
admin.privileges.show_privileges()




