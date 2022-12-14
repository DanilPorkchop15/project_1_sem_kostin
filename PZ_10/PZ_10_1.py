# вариант 12
# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.
# Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента
# – печенье, молоко, сыр, сметана.
# Определить:
# 1. в каких магазинах нельзя приобрести сметану.
# 2. какие товары из магазина Магнит отсутствуют в магазине Перекресток.
# 3. какие товары из магазина Лента отсутствуют в магазине Магнит.

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
notInPerekrestok = magnit - perekrestok
print("в перекрестке нет товаров из магнита:", *notInPerekrestok)

# задание 3
notInMagnit = lenta - magnit
print("в магните нет товаров из ленты:", *notInMagnit)
