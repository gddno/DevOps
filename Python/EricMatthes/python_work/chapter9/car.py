class Car():
    def __init__(self,make,model,year):
	    self.mk = make
	    self.md = model
	    self.y = year
	    self.odometr_reading = 25

    def get_descriptive_name(self):
	    long_name = str(self.y) + " " + self.mk.title() + " " + self.md.title()
	    return long_name
    
    def read_odometer(self):
	    print("This car has " +str(self.odometr_reading)+" miles on it.")

    def update_odometr(self, milleage):
	    if milleage >= self.odometr_reading:
		    self.odometr_reading = milleage
	    else:
		    print("Ne nayubui systemU")
    def increment_odometr(self, miles):
	    if miles >= 0:
		    self.odometr_reading += miles
	    else:
		    print("Nelza vvodit otricatelnye znazhenia")
	    

my_new_car = Car('mersedes','e',2023)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometr(26)
my_new_car.read_odometer()
my_new_car.increment_odometr(10)
my_new_car.read_odometer()