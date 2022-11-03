# вариант 12
# составить функцию суммирования числового ряда
def summ(a):
    return sum(a))


try:
    nums = map(int, input('Введите ряд чисел через пробел: ').split())
    print(summ(nums))
except Exception as ex:
    print('Произошло исключение: ', ex)
