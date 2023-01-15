class Car():
    def __init__(self,made,mark,color):
	    self.made = made
	    self.mark = mark
	    self.color = color
    def print_characteristic(self):
	    print("list: "+self.made.title()+" "+ self.mark.title()+" "+self.color.title())

class Battery():
    def __init__(self, battery_size = 70):
	    self.size_battery = battery_size
    def describe_battery(self):
	    print("This car have a " + str(self.size_battery) + "-kWh battery.")
    def upgrade_battery(self):
	    if self.size_battery != 85:
		    self.size_battery = 85
	    else:
		    print("Size bettery is 85 thise OK")

class ElectricCar(Car):
    def __init__(self,made,mark,color):
	    super().__init__(made,mark,color)
	    self.battery = Battery()


my_car = ElectricCar('Mersedes', 'e', 'black')
my_car.print_characteristic()
my_car.battery.describe_battery()
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.upgrade_battery()
