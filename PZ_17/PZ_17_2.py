# Вариант 12
# Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
# выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
# свойство "тип кузова".
class Transport:
    def __init__(self, brand, model, release_date):
        self.brand = brand
        self.model = model
        self.release_date = release_date

    def __str__(self):
        return f'марка: {self.brand}; модель: {self.model}; год выпуска: {self.release_date}'


class Automobile(Transport):
    def __init__(self, brand, model, release_date, k_type):
        super().__init__(brand, model, release_date)
        self.k_type = k_type

    def __str__(self):
        return f'марка: {self.brand}; модель: {self.model}; год выпуска: {self.release_date}; тип кузова: {self.k_type}'


trans = Transport('BMX', 'Ultra', 2018)
car = Automobile('Man', 'Super', 2021, 'КРУТОЙ!!!')
print(trans)
print(car)
