class Person:
    """Это класс Person для работы с информацией о сотруднике"""

    def __init__(self, name, surname, classif=1):
        self.name: str = name
        self.surname: str = surname
        self.classif: int = classif

    def info(self):
        return f'Имя: {self.name}; Фамилия: {self.surname}; Классификация: {self.classif};'

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}')


Clark = Person('Clark', 'Kent', 4)
Carl = Person('Carl', 'Great', 2)
Kirk = Person('Kirk', 'Hammet')
print(f'{Person.info(Clark)}\n{Person.info(Carl)}\n{Person.info(Kirk)}')
del Kirk

