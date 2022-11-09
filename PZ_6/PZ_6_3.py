try:
    lst = [i+1 for i in range(int(input()))]
    print(lst)
    k = int(input())
    if 1 < k < n:
        for j in range(k):
            lst = lst[-1:]+lst[:-1]  # добавление к значению списку из последнего индекса остального скиска
        print(lst)
    else:
        print('no.')
except Exception as ex:
    print(ex)
