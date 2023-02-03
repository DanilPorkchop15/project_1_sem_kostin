# Вариант 12.
# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.
from random import randint

matrix = [[randint(-10, 10) for j in range(5)] for i in range(5)]
# сбор списка из негативных элементов с помощью перебора каждого элемента в каждой строке в матрице
negative = [elem for row in matrix for elem in row if elem < 0]
print('Вывод матрицы(5*5): ')
for i in matrix:
    print(i)

print('Длина списка отрицательных элементов', len(negative))
