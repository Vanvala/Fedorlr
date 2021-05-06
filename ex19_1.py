class Cat():
    name = ''
    color = ''
    weight = 0

    def meow(self):
        print(self.name, ' say meow!')

myCat = Cat()
myCat.name = 'Kotja'
myCat.color = 'red'
myCat.weight = 1
myCat.meow()
