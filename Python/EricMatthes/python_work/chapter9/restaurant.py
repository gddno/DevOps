class Restaurant():
    def __init__(self, name_restaurant, cuisine_tipe):
	    self.name = name_restaurant
	    self.cuisine = cuisine_tipe
	    self.number_served = 100
    def describe_restaurant(self):
	    print("\nName our restaurant's " + self.name.title() + ".")
	    print("And we have " + self.cuisine + " type cuisine.")
    
    def open_restaurant(self):
	    print("\nAnd restaraunt " + self.name.title() + " how specialisation's " + self.cuisine + " cuisine is OPEN!!!")
    
    def number(self):
	    print("\nCount = "+str(self.number_served)+".")
    
    def set_number(self, number):
	    if number >= self.number_served:
		    self.number_served = number
	    else:	
		    print("Ne byvaet otricatelnogo collichestva!!!!")
    
    def increment_number(self,inc):
	    if inc <= 0:
		    print("Nelza ubalvlat gostei")
	    else:
		    self.number_served += inc

