class Nikola:

    def __init__(self, name, age):
        self.name = 'Николай'
        self.age = age

        if name != 'Николай':
            print(f'Я не {name}, а {self.name}')


bro = Nikola('Макака', 16)
Nikolai = Nikola('Николай', 1000)
print(bro.__dict__)