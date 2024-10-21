"""class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print(self.name)
        self.sound = "Bark"
        print(self.sound)
        
class Dog(Animal):
    def speak(self):
        super().speak()
        
obj_1 = Dog("Dog")
obj_1.speak()  


class Teacher:
    def __init__(self):

        self.computer = "computer"
class Researcher:
    def __init__(self):
        
        self.computerfildes = "computerfildes"
class TeachingResearcher(Teacher,Researcher):
    def __init__(self):
        Teacher.__init__(self)
        Researcher.__init__(self)
    def display(self):

        print(self.computer)
        print(self.computerfildes)
obj = TeachingResearcher()
obj.display()


class Bird:
    def __init__(self):
        self.species = "species"
class Flayable:
    def __init__(self):
        self.fly = "Flying"
class Eagle(Bird,Flayable):
    def __init__(self):
        Bird.__init__(self)
        Flayable.__init__(self)
    def display(self):
        print(self.species)
        print(self.fly)
obj = Eagle()
obj.display()

class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
class Developer(Employee):
    def __init__(self,name,salary,language):
        Employee.__init__(self,name,salary)
        self.language = language
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        Employee.__init__(self,name,salary)
        self.team_size = team_size
class Inten(Developer):
    def __init__(self,name,salary,language,internship):
        Developer.__init__(self,name,salary,language)
        self.internship = internship
    def display(self):
        print(self.name,self.salary,self.language,self.internship)
obj = Inten("sindu",30000,"Python","3 months")
obj.display()



class Vehicle:
    def __init__(self,brand,module):
        self.brand = brand
        self.module = module
class Car(Vehicle):
    def __init__(self, brand, module,num_doors):
        Vehicle.__init__(self,brand,module)
        self.num_doors= num_doors
        print(self.brand,self.module,self.num_doors)
class Bike(Vehicle):
    def __init__(self, brand, module,capacity):
        Vehicle.__init__(self,brand,module)
        self.capacity = capacity
        print(self.brand,self.module,self.capacity)
obj1 = Bike("Pulsur","N1",50000)
odj2 = Car("Benz","B2",2000000)

    
class Device:
    def __init__(self,name):
        self.name = name
class Phone(Device):
    def __init__(self, name,pno):
        Device.__init__(self,name)
        self.pno = pno
class Tablet(Device):
    def __init__(self, name,screen):
        Device.__init__(self,name)
        self.screen = screen
    def c1(self):
        print(self.name,self.screen)
class SmartPhone(Phone,Tablet):
    def __init__(self,name,pno,screen,os):
        Phone.__init__(self,name,pno)
        Tablet.__init__(self,name,screen)
        self.os = os
    def display(self):
        print(self.name,self.pno,self.screen,self.os)
obj = SmartPhone("Iphone",9999999998,"2inches","tizen")
obj.display()
obj.c1

"""
a = sindu .split()
print(a)