# вариант 12
# составить функцию суммирования числового ряда
def summ(a):
    print(sum(a))


try:
    nums = map(int, input('Введите ряд чисел через пробел: ').split())
    summ(nums)
except Exception as ex:
    print(ex)
