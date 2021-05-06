class Animal:
    name = ""
    def __init__(self, name):
        self.name = name
        print("Родилось новое животное", self.name)
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def makeNoise(self):
        print(self.name, 'говорит Гррр')

    def eat(self):
        print('Ням-ням')

    
goat = Animal('Byzja')
goat.getName()
goat.setName('Milka')
goat.eat()
goat.makeNoise()