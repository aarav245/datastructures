#inheritence: parent class
class car:
    def __init__(self,color,date,miles,brand):
        self.brand = brand
        self.color = color
        self.date = date
        self.miles = miles
        self.brand = brand
    def display(self):
        print(self.brand)
        print(self.color)
        print(self.date)
        print(self.miles)
        print(self.brand)
#child class
class sedan(car):
    def __init__(self,color,date,miles,brand,height,width):
        super().__init__(color,date,miles,brand)
        self.height = height
        self.width = width
    def display(self):
        print(self.brand)
        print(self.color)
        print(self.date)
        print(self.miles)
        print(self.brand)
        print(self.height)
        print(self.width)
car1 = car("blue",1966,432554,"toyota")
car1.display()
sedan1 = sedan("black",2011,50561,"Audi","57 inches", "75 inches")
sedan1.display()