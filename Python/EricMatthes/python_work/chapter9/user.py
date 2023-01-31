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



