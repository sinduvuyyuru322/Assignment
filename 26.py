class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def update(self):
        self.age = input()
name = input()
age = input()
gender = input()
s = person(name,age,gender)
s.update()
print("Name : " +s.name + " AGE : " +s.age +" Gender : "+s.gender)




class company:
    count = 0
    def __init__(self):
        company.dict = {}
    def add_ele(self,name,department):
        company.count+=1
        company.dict[name] = department
    def total_employes(self):
        print(self.count)

name = input()
department = input()
new_com = company()
new_com.add_ele(name,department)
new_com.total_employes()



class rectangle:
    def __init__(self):
        self.length = 10
        self.width = 20
    def calcuate_area(self):
        #global a to make it use out of the class
        a = (self.length+self.width)*2
        print(a)
call_fun = rectangle()
call_fun.calcuate_area()
#print(a)"""


class employee:

    def __init__(self,list):
        self.a = list.keys()
        self.b = list.values()
    def total_salary(self):
        self.empty = {}
        bonus_amount = 2000
        for i,j in list.items():
           self.empty[i] = j+bonus_amount

list = eval(input())
just = employee(list)
just.total_salary()
print(just.empty)