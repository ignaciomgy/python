class Animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating') 

    def speak(self):
        raise NotImplementedError('Error this abstract method should be defined on the class')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')   

    #redefinimos un metodo de la clase heredada
    def who_am_i(self):
        print('I am a Dog =)')

    def bark(self):
        print('WOOFF')

    def speak(self):
        return self.name + ' is my name'

class Cat(Animal):
    def speak(self):
        return self.name + ' is my name'


#-----------------------------

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()