from Hero import *

myhero = Hero("Vova Putin", 100, "Human")
mySuperHero = SuperHero("Dima Medvedev", 40, "Orc", 5)
car = Cars("BMW", "X5", "black")

myhero.show_hero()
mySuperHero.make_magic()
mySuperHero.show_hero()
mySuperHero.magic = 10
mySuperHero.show_hero()
car.show_car()
car.transmission_up()
car.speed_increase()
car.show_car()