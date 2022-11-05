# вариант 12
# составить функцию суммирования числового ряда
def summ(a):
    summa = 0
    i = len(a)
    while i > 0:
        summa += a[i-1]
        i -= 1
    return summa


try:
    nums = list(map(int, input('Введите ряд чисел через пробел: ').split()))  # ввод чисел через пробел в список
    print(summ(nums))
except Exception as ex:
    print('Произошло исключение: ', ex)
