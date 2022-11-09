import random

try:
    listA = [random.randint(1, 100) for i in range(int(input()))]   
    print(listA)
    if len(listA) == 2:
        print(*listA)
    elif len(listA) < 2:
        print()
    else:
        SumMax = listA[1] + listA[2]
        k = 2
        for i in range(1, len(listA)):
            if (listA[i - 1] + listA[i]) > SumMax:
                k = i
                SumMax = listA[i - 1] + listA[i]
        print(listA[k - 1], ' ', listA[k])
except Exception as ex:
    print(ex)
