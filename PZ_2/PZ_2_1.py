# вариант 12
# Дано двузначное число. Найти сумму и произведение его цифр
while True:  # запуск бесконечного цикла для повторного ввода данных при исключениях
    try:
        num = int(input('Введите двузначное целое число: '))  # ввод целочисленного значения
        if 9 < num < 100:  # проверка условия принадлежности числа к разряду двузначных
            print('Сумма цифр Вашего числа: ', num//10 + num % 10)
            print('Произведение цифр Вашего числа: ', (num//10) * (num % 10))
            break  # прерывание цикла при выполнении условия
        else:
            print('Пожалуйста, введите двузначное число.')
    except ValueError:  # обработка несоответствия величин
        print('Введите число в целочисленном формате, пожалуйста.')
