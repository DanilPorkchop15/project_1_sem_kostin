# вариант 12
# составить функцию суммирования числового ряда
def summ(a):
    i = 0
    summa = 0
    while a > i:
        i += 1
        summa += i
    return summa


while True:
    try:
        nums = int(input('Введите длину числового ряда: '))  # ввод длины числового ряда
        print(summ(nums))
        break
    except Exception as ex:
        print('Произошло исключение: ', ex)
