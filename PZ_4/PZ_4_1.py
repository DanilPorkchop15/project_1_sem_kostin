n = int(input("Введите число: "))
digit = 1
result = 0
i = 0
while n >= i:
    digit += 0.1
    while i+1 % 2 != 0:
        result += digit
        break
    while i+1 % 2 == 0:
        result -= digit
        break
    i += 1
print(result)
