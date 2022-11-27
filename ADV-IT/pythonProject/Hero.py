from pydoc import describe


class Hero():
    """Class to creat Hero for our Game"""

    def __init__(self, name, level, race):
        """Initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all aprametrs of this Hero"""
        discription = (self.name + " " + "Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level += 1
    
    def move(self):
        """Start moving Hero"""
        print("Hero " + self.name + " start moving...")

    def harm(self):
        """Harm to my Hero"""
        self.health -= 1

    def set_health(self, new_health):
        self.health = new_health


#---------------------------------------------------------------------

class SuperHero(Hero):
    def __init__(self, name, level, race, magic_level):
        """Initiate our Super Hero"""
        super().__init__(name,level,race)
        self.magic_level = magic_level
        self.__magic = 100

    def make_magic(self):
        """Use magic"""
        self.__magic -= 10

    def show_hero(self):
        discription = (self.name + "Level is: " + str(self.level) + " Race is : " + self.race + " Health is : " + str(self.health)
                       + " Magic is : " + str(self.__magic)).title()
        print(discription)

#-----------------------------------------------------------------------


class Cars():
    def __init__(self, brand, model, color):
        """Initiate our Cars"""
        self.brand = brand
        self.model = model
        self. color = color
        self.speed = 0
        self.number_of_wheels = 4
        self.transmission = 1

    def transmission_up(self):
        self.transmission += 1
    def transmission_down(self):
        self.transmission -= 1
    def speed_decrease(self):
        self.speed -= 10
    def speed_increase(self):
        self.speed += 10
    def show_car(self):
        discription = (self.brand + " Model is: " + self.model +" Number of wheals:  "+ str(self.number_of_wheels) +
                       " Color is: " + self.color + " And speed is: " + str(self.speed) +
                       " else transmission: " + str(self.transmission)).title()
        print(discription)