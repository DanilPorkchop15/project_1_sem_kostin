# вариант 12
# Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
# и вывести эти элементы в порядке возрастания их индексов.
import random

try:
    listA = [random.randint(1, 100) for i in range(int(input('Введите длину списка: ')))]
    print(f'Ваш список:\n{listA}')
    if len(listA) == 2:
        print(*listA)
    elif len(listA) < 2:
        print('Не получится найти сумму значений < 2')
    else:
        SumMax = listA[1] + listA[2]
        k = 2
        for i in range(1, len(listA)):
            if (listA[i - 1] + listA[i]) > SumMax:
                k = i
                SumMax = listA[i - 1] + listA[i]
        print(f'Соседние числа с наибольшей суммой: {listA[k - 1]} и {listA[k]}')
except Exception as ex:
    print('Произошла ошибка: ', ex)
