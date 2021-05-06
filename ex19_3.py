class StringVar:
    name = ''

    def __init__(self, name):
        self.name = name

    def set(self, new):
        self.name = new

    def get(self):
        return self.name
        # print(self.name)


StringVar('None')

StringVar.set('Hi', 'There')
StringVar.get()
StringVar.set('Hello')
StringVar.get()
