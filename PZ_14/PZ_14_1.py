# Вариант 12
# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
import re

# даты с .
dotDates = re.compile(r"[0-3]\d\.[0-1]\d\.\d\d\d\d")
# даты с /
slashDates = re.compile(r"[0-3]\d/[0-1]\d/\d\d\d\d")
# даты февраля с /
slashDatesFeb = re.compile(r"[0-3]\d/02/\d\d\d\d")

f = open('dates.txt')
text = f.read()
dotDList = dotDates.findall(text)
slashDList = slashDates.findall(text)
slashFeb = slashDatesFeb.findall(text)
f.close()

print(f'Даты с "."{dotDList}\n')
print(f'Даты с "/"\n{slashDList}\n')
print(f'Даты февраля с "/"\n{slashFeb}\n')

print('Количество дат с ".": ', len(dotDList))
print('Количество дат с "/": ', len(slashDList))

f = open('fedDatesSlash.txt', 'w+')
for i in slashFeb:
    f.write(i+'\n')