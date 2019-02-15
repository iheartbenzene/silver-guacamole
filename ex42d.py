## Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has-a name
        self.name = name

##Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a name
        self.name = name

##Person is-a object
class Person(object):

    def __init__(self, name):
        ##person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##epmloyeaa has-a name
        super(Employee, self).__init__(name) #what is this fuckery?
        ##employee has-a salary
        self.salary = salary

##fish is-a object
class Fish(object):
    pass

##salmon is-a fish
class Salmon(Fish):
    pass

##halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

##mary has-a pet named satan that is-a cat
mary.pet = satan

##frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

##frank has-a pet named rover that is-a dog
frank.pet = rover

##flipper is-a fish
flipper = Fish()

##crouse is-a salmon that is-a fish
crouse = Salmon()

##harry is-a halibut that is-a fish
harry = Halibut()
