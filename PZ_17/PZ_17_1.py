# Вариант 12
# Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
# выводит информацию о животном в формате "Имя: имя, Вид: вид".
class Animal:
    def __init__(self, name, vid):
        self.name = name
        self.vid = vid

    def display_info(self):
        print(f'Имя: {self.name}, Вид: {self.vid}')


cat = Animal('кот', 'кошачьи')
dog = Animal('Собакакка', 'собачьи')
cat.display_info()
dog.display_info()
