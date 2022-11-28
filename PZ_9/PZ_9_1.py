dic = {"Hello": "Привет",
       "Bye": "Пока",
       "Name": "Имя",
       "Surname": "Фамилия",
       "Father": "Отец",
       "Mother": "Мать",
       "Uncle": "Дядя",
       "Aunt": "Тетч",
       "Cat" : "Кот",
       "Dog" : "Собака"}
for key, value in dic.items():
    print(key, "- это", value)
word = input('Введите английское слово: ')
if word in dic:
    print(dic[word])
