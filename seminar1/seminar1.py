import math
import csv
### исключения #########################################################################################################


def find_file(file_name):
    """ only txt format """
    try:
        f = open(file_name, "r")
        print(*f)
    except FileNotFoundError:
        print(f"404. File {file_name} not found")


def multiplication(*args):
    try:
        args = list(args)
        count = 1
        for i in args:
            if isinstance(i, int):
                count *= i
            raise ValueError
        print(count)
        return count
    except ValueError:
        print("impossible")


# multiplication(2, 3, 4, "5", 6)


def calc(string):
    string = string.split(" ")
    n1 = int(string[0])
    n2 = int(string[2])
    if string[1] == "+" :
        print(f"{n1} + {n2} --> {n1 + n2}")
    elif string[1] == "-":
        print(f"{n1} - {n2} --> {n1 - n2}")
    elif string[1] == "*":
        print(f"{n1} * {n2} --> {n1 * n2}")
    elif string[1] == "/":
        if int(string[2]) != 0:
            print(f"{n1} / {n2} --> {n1 / n2}")
        else:
            print("division by zero!!!")
    elif string[1] == "%":
        if int(string[2]) != 0:
            print(f"{n1} % {n2} --> {n1 % n2}")
        else:
            print("division by zero!!!")
    elif string[1] == "^":
        print(f"{n1} ^ {n2} --> {n1 ** n2}")
    else:
        print("mistake")


# calc("13 - 5")


def calcMatrixDiagonalSumm(*matrix):
    try:
        count = 0
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if row == column:
                    print(format(matrix[row][column]))
                    # count = count + matrix[row][column]
        print(count)
    except IndexError:
        print("Матрица не является квадратной")


# calcMatrixDiagonalSumm([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def triangle(tuple1, tuple2, tuple3):
    if tuple1[0] != tuple2[0] != tuple3[0] or tuple1[1] != tuple2[1] != tuple3[1]:
        a = math.sqrt((tuple1[0]-tuple2[0])**2 + (tuple1[1] - tuple2[1])**2)
        b = math.sqrt((tuple1[0]-tuple3[0])**2 + (tuple1[1] - tuple3[1])**2)
        c = math.sqrt((tuple3[0]-tuple2[0])**2 + (tuple3[1] - tuple2[1])**2)
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(s)
    else:
        print("mistake")
    # s = ((tuple1[0] - tuple3[0])*(tuple2[1] - tuple3[1]) - (tuple2[0] - tuple3[0])*(tuple1[0] - tuple3[1]))/2
    # print("S =", s)


# triangle((1, 6), (9, 6), (10, 9))


### генераторы #########################################################################################################


l1 = ['1', '123', '123', '12', '1', '123']
l2 = [2, 4, -2, -3, 0, 11, 3, -1]

d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}

# элемент списка - количество символов в строке
lst1 = [len(x) for x in l1]
# print(1, lst1)

# количестыво элементов списка, длина которых больше 2
lst2 = [x for x in l1 if len(x) > 2]
# print(2, lst2)

# все элементы списка умножены на индекс
lst3 = [l2[x] * x for x in range(len(l2))]
# print(3, lst3)

# удалить отрицательные значения
lst4 = [x for x in l2 if x >= 0]
# print(4, lst4)

# заменить отрицательные числа на их индекс
lst5 = [l2[i] if l2[i] > 0 else i for i in range(len(l2))]
# print(5, lst5)

# словарь буква: индекс, буквы не повторяются
s = "abcde"
dict1 = {s[i]: i for i in range(len(s))}
# print(6, dict1)

# определить, сколько элементов списка содержится в словаре
x = 0
lst6 = []


### функции ############################################################################################################


### CSV ############################################################################################################






































