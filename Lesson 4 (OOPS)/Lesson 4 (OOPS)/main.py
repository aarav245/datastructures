#Creating class
class student:
    def __init__(self,name,age,grade,height,weight):
        self.name = name
        self.age = age
        self.grade = grade
        self.height = height
        self.weight = weight
    def printclass(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.height)
        print(self.weight)
    def change(self):
        self.name = input("Enter a new name: ")
        self.age = input("Enter a new age: ")
        self.grade = input("Enter a new grade: ")
        self.weight = input("Enter a new weight: ")
        self.height = input("Enter a new height: ")
student2 = student("Ryan",12,"7th","5 feet", "80 lbs")
#creating an object
student1 = student("Matthew",15,"10th","5 feet 2 inches", "95 lbs")
student1.printclass()
student2.printclass()
student1.change()
student1.printclass()