import csv

# вариант 4


Red = '\033[48;05;009m'  # escape - последовательности
White = '\033[48;05;015m'
Black = '\033[48;05;000m'
End = '\033[0m'
n = 3
count = 0
bfr = 0


def Diagram():  # Функция для вывода диаграммы
    e = 'Книги после 2017 года '
    s = 'Книги до 2017 года '
    m = len(e) + 31 + 3
    print(White + ' ' * m + End)
    print(
        White + s + White + ' ' * (len(e) - len(s)) + Red + '   ' * p1 + White + ' ' * (m - len(e + '   ' * p1)) + End)
    print(White + ' ' * m + End)
    print(White + e + Red + '   ' * p2 + White + ' ' * (m - len(e + '   ' * p2)) + End)
    print(White + ' ' * m + End)
    print(White + ' ' * (len(e) - 1) + End + White + '0 10 20 30 40 50 60 70 80 90 100  %' + End)


def Diagram_en():  # Функция для вывода диаграммы (Для books-en)
    e = 'Книги после 2000 года '
    s = 'Книги до 2000 года '
    m = len(e) + 31 + 3
    print(White + ' ' * m + End)
    print(
        White + s + White + ' ' * (len(e) - len(s)) + Red + '   ' * p1 + White + ' ' * (m - len(e + '   ' * p1)) + End)
    print(White + ' ' * m + End)
    print(White + e + Red + '   ' * p2 + White + ' ' * (m - len(e + '   ' * p2)) + End)
    print(White + ' ' * m + End)
    print(White + ' ' * (len(e) - 1) + End + White + '0 10 20 30 40 50 60 70 80 90 100  %' + End)


def flag():  # Функция для вывода флага
    for i in range(5):
        print(White + ' ' * 40 + End)
    for i in range(5):
        print(Red + ' ' * 40 + End)
    print()


def uzorchik():  # Функция для вывода узора
    print((Black + ' ' * 43 + End) * n)
    for i in range(2):
        print((End + ' ' * 20 + Black + ' ' * 3 + End + ' ' * 20) * n)
    print((Black + ' ' * 43 + End) * n)
    print((End + ' ' * 6 + Black + ' ' * 3 + End + ' ' * 25 + Black + ' ' * 3 + End + ' ' * 6) * n)
    print((Black + ' ' * 43 + End) * n)


def function():  # Функция для вывода функции
    lines = [[0 for _ in range(10)] for _ in range(9)]
    result = [0 for _ in range(10)]
    for i in range(10):
        result[i] = i ** 0.5
    step = round((result[9] - result[0]) / 9, 1)
    for j in range(9):
        lines[j][0] = round(step + step * j, 1)
    for i in range(9):
        for j in range(1, 10):
            if abs(lines[i][0] - result[j]) < 0.3:
                lines[i][j] = 1
    for i in range(8, -1, -1):
        lin = ''
        for j in range(10):
            if j == 0:
                lin += White + str(lines[i][j])
            if lines[i][j] == 0:
                lin += '  '
            elif lines[i][j] == 1:
                lin += Red + '  ' + White
        lin += End
        print(lin)
    print(White + '0   1 2 3 4 5 6 7 8 9' + End)


a = input('Вывести флаг Польши(Да/Нет)? :')
if a == 'Да':
    print(f'Флаг Польши :\n')
    flag()
a = input('Вывести узор(Да/Нет)? :')
if a == 'Да':
    print(f'Узор :\n')
    uzorchik()
a = input('Вывести график функции y = x^0.5 (Да/Нет)?:')
if a == 'Да':
    print(f'График Функции :\n')
    function()

print('\nДиаграмма для books.csv\n')
with open('books.csv', encoding='cp1251') as r_file:
    book_list = csv.DictReader(r_file, delimiter=';')
    for row in book_list:
        count += 1
        if int(row["Дата поступления"][:4]) <= 2017:
            bfr += 1
p1 = round(int(round(bfr / count, 2) * 100), -1) // 10  # процент книг до 2017
p2 = 10 - p1  # процент книг после 2017
Diagram()

count_en = 0
bfr_en = 0
print('\nДиаграмма для books-en.csv\n')
with open('books-en.csv', encoding='cp1251') as r_file:
    book_list = csv.DictReader(r_file, delimiter=';')
    for row in book_list:
        count_en += 1
        if len(row["Year-Of-Publication"]) == 4:
            if int(row["Year-Of-Publication"]) <= 2000:
                bfr_en += 1

p1 = round(int(round(bfr_en / count_en, 2) * 100), -1) // 10  # процент книг до 2000
p2 = 10 - p1  # процент книг после 2000
Diagram_en()
