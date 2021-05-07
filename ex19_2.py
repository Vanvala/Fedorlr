class Animal:
    name = ""

    def __init__(self):
        print("Родилось новое животное", self.name)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def make_noise(self):
        print(self.name, 'говорит Гррр')

    def eat(self):
        print('Ням-ням')


class Cat(Animal):
    def __init__(self):
        print('Родился кот')
        Animal.__init__(self)

    def make_noise(self):
        print(self.name, 'Говорит Мяу')


class Dog(Animal):
    def __init__(self):
        print('Родилась собака')
        Animal.__init__(self)


    def make_noise(self):
        print(self.name, 'Говорит Гав')


goat = Animal()
cat_1 = Cat()
cat_2 = Cat()
dog = Dog()
goat.name = 'Bizja'
cat_1.name = 'Kotja'
cat_2.name = 'Vasja'
dog.name = 'Sharik'
goat.eat()
goat.make_noise()
cat_2.eat()
cat_1.make_noise()
dog.eat()
dog.make_noise()