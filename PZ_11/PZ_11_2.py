# вариант 12
# 2. Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно вставив после каждой строки строку из символов
# «*».

file1 = open('text18-12.txt', encoding='UTF-8')
# print(file1.read())
spaces = 0
lines = []
for i in file1:
    print(i.strip())
    lines.append(i.strip())
    for j in i:
        if j == ' ':
            spaces += 1
print('\nКоличество пробельных символов:', spaces)
file1.close()

file2 = open('task-11-2-1.txt', 'w+', encoding='UTF-8')
for i in lines:
    file2.write(i + '\n')
    file2.write('*' * 20 + '\n')
file2.close()