def summ(a):
    print(sum(a))


while True:
    try:
        nums = map(int, input().split())
        summ(nums)
        break
    except Exception as ex:
        print(ex)
