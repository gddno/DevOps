class CountGirls():
	
	def __init__(self,name,age,price):
		self.name = name.title()
		self.age = age
		self.price = price

	def up_price(self, amount = 500):
		#amount = int(input('Enter how match you spend on hes: '))
		self.price += amount
		#print("\nDima Hi!!! Name your girl friend " + self.name + " and hes age is " +
		#str(self.age) + " and you spend on hes " + str(self.price) + "$. Hahahah, you are mudak!!!" )

my_girl = CountGirls('nastya', 26, 2000)
my_girl.up_price()