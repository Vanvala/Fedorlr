class StringVar:

    def __init__(self, name):
        self.name = name

    def set(self, new):
        self.name = new

    def get(self):
        print(self.name)


st = StringVar('None')

st.set('Hi')
st.get()
st.set('Hello')
st.get()
