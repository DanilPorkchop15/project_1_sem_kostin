# вариант 12
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Среднее арифметическое элементов первой трети:

from random import randint

num = [randint(-10, 10) for i in range(10)]
numThird = num[0:round(len(num) / 3)]

file1 = open('task-11-1-1.txt', 'w+')
file1.write(str(num))
file1.close()

file2 = open('task-11-1-2.txt', 'w+')
file2.write(f'Исходные данные: {num}\n')
file2.write(f'Количество элементов: {len(num)}\n')
file2.write(f'Максимальный элемент: {max(num)}\n')
file2.write(f'Среднее арифметическое элементов первой трети: {sum(numThird) / len(numThird)}')
file2.close()