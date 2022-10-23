# TASK 1
# Пользователь вводит имя файла (например "notes.txt") и новое расширение (например, 'log').
# Напечатайте на экране имя файла с новым расширением, т.е. в данном случае "notes.log".
# Расширением файла считайте строку после самой правой точки, т.е. в имени "файл.тхт.пп" - расширение это "пп"
# Учтите, что в имени файла точка может встречаться несколько раз, а сам файл может не иметь расширения вовсе.

def changeExpansion(fileName, newExpansion):
    index = fileName.rindex(".")
    newFileName = fileName[:index+1] + newExpansion
    print(newFileName)


# changeExpansion("файл.тхт.пп", "log")


# * Добавьте к итоговому имени файла длину его имени без расширения через подчеркивание, т.е. для файла "notes.txt"
# и расширения 'log' итог будет "notes_5.log". Предусмотрите различные ошибки со стороны пользователя.
# Например, пользователь может вводить расширение как с точкой, так и без точки и корректно это обработайте
# !!(т.е. возможен ввод как '.log', так и 'log'), пользователь может забыть что-то ввести и т. п.

def changeExpansion2(fileName, newExpansion):
    index = fileName.rindex(".")
    newFileName = fileName[:index] + "_" + str(index) + "." + newExpansion
    print(newFileName)


# changeExpansion2("notes.txt", "log")


# TASK 2
# Дан список чисел (задайте его сами). Напечатайте все числа большие 0, но меньшие 100.

lst = [5, 8, -13, 5, 5, 4, 4, 4, 4, 8, -322, 748]
newLst = [x for x in lst if 0 < x < 100]
# print(newLst)


# * Дан список - удалите все одинаковые элементы, если они больше 0
def delPossitiveDublicates(lst):
    lst = sorted(lst)
    print(lst)
    for i in range(len(lst)):
        if lst[i] < 0:
            continue
        else:
            index = i
            break

    result = lst[:index] + list(set(lst[index:]))
    print(result)


delPossitiveDublicates([5, 8, -13, 5, 5, 4, 4, 4, 4, 8, -322, 748])


# ** Пользователь вводит список чисел (заранее неизвестно сколько их). Конец ввода по вводу слова "end".
# Найдите второй максимальный элемент в этом списке (т.е. для списка [1,6,3,0] ответ 3).

def findSecondMaxValue():
    userList = []
    element = input()

    while element != "end":
        try:
            element = input()
            userList.append(int(element))
        except ValueError:
            print("введено не число!!!")
    print(userList)

    userList = sorted(userList)
    print(userList)
    print(userList[-2])


# TASK 3
# Задайте 4 списка names (содержит список имён), surnames (содержит список фамилий), ips (содержит список IP-адресов),
# logins (содержит список логинов) любым удобным для вас образом (можно вручную, прочитать из какого-либо файла,
# запросом у пользователя). Представим, что данные из этих списков уже лежат в необходимом порядке.
# Сохраните данные в файл в формате JSON

names = ["", "", "", "", "", "", "", "", "", ""]
surnames = ["", "", "", "", "", "", "", "", "", ""]
ips = ["", "", "", "", "", "", "", "", "", ""]
logins = ["", "", "", "", "", "", "", "", "", ""]




# TASK 4
# Написать программу, читающую информацию из всех файлов с указанным расширением в указанной директории.
# Прочитанную информацию сохранить в лог-файл


import os
import logging

# справка
# #просто найти файлы.csv
# for f in os.scandir('C:\Users\Тамара\PycharmProjects\практикум\seminar2.py'):
#     if f.is_file() and f.path.split('.')[-1].lower() == 'csv':
#         print(f.path)
#
# #прочитать содержимое
# for f in os.scandir('Ваш_путь_к_директории'):
#     if f.is_file() and f.path.split('.')[-1].lower() == 'csv':
#         with open(f.path, 'r') as csvfile:
#             print(csvfile.read())
























