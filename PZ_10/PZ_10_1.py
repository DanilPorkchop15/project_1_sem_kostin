# вариант 12

magnit = {"молоко", "соль", "сахар", "печенье", "сыр"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар", "печенье"}
lenta = {"печенье", "молоко", "сыр", "сметана"}

# задание 1
noSmetanaShops = set()
if "сметана" not in magnit:
    noSmetanaShops.add("магнит")
if "сметана" not in pyaterochka:
    noSmetanaShops.add("пятерочка")
if "сметана" not in perekrestok:
    noSmetanaShops.add("перекресток")
if "сметана" not in lenta:
    noSmetanaShops.add("лента")
print("сметаны нет в магазинах: ", *noSmetanaShops)

# задание 2
notInPerekrestok = set()
for i in magnit:
    if i not in perekrestok:
        notInPerekrestok.add(i)
print("в перекрестке нет товаров из магнита:", *notInPerekrestok)

# задание 3
notInMagnit = set()
for i in lenta:
    if i not in magnit:
        notInMagnit.add(i)
print("в магните нет товаров из ленты:", *notInMagnit)
