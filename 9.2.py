#class attribute shave by all object mean one bersion and all should share
#create student class name age gender create getter and seter

class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def set_age(self):
        age=self.age


student1=student("Zosia",19,"Female")
student2=student("Josie",39,"Male")
student3=student("Jimmy",20,"Male")

#
mydog.gasp(3)

student2.get_name()
student3.set_age(100)
print(student3.name)
print(student3.age)
print(student1.name)
print(student1.age)
print(student1.gender)
print(student2.name)
print(student2.age)
print(student2.gender)

doglist:["Cocoa","Jack","Juzio"]

for dog in doglist:
    print(dog) #autimatically calls string method


class Nursing:
    def __init__(self):
        self.Dog=[]


    def addDogs(self,name):
        self.Dog.append(name)


