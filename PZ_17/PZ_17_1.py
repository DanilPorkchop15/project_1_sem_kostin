class Animal:
    def __init__(self, name, vid):
        self.name = name
        self.vid = vid

    def display_info(self):
        print(f'Имя: {self.name}, Вид: {self.vid}')


cat = Animal('кот', 'кошачьи')
cat.display_info()