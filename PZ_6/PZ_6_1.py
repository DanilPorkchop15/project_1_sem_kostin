import random
try:
    a = [random.randint(1, 100) for i in range(int(input('Введите длину списка (нечетное положительное число): ')))]

    while len(a) % 2 == 0:
        print('Нужно ввести целое нечетное положительное значение длины списка!')
        quit()
    print('Ваш список: \n', a)
    print('Нечетные номера Вашего списка в порядке убывания:\n', a[-1::-2])
except Exception as ex:
    print('произошла ошибка:\n', ex)
