# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("\nЗадание-1")

def parsing_num(num):
    #Проверяем на отрицательность
    Otric = False
    if num[0] == '-':
        Otric = True
        num = num[1:]
    l = num.split()
    R = 0
    for item in l:
        if len(item.split("/")) >1:
            chislit = item.split("/")[0]
            znamen = item.split("/")[1]
            item = int(chislit)/int(znamen)
        R += float(item)
    if Otric == True:
        R = -R
    #print(R)
    return R


#Тело программы***********************************************
Operations = ["+", "-"]
formula = "-2 5/6 - -4 4/7"
for Operation in Operations:
    Operands = formula.split(" {} ".format(Operation))
    if len(Operands) > 1:
        break

else:
    print("Строка не соответсвует формату")
    exit()
Res = 0
for i,Operand in enumerate(Operands):
    if i == 0:
        Res = parsing_num(Operand)
    else:
        if Operation == "+":
            Res += parsing_num(Operand)
        elif Operation == "-":
            Res -= parsing_num(Operand)
    print("Операнд {}:".format(i+1),round(parsing_num(Operand), 3))

print("Результат:",round(Res, 3))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print("\nЗадание-2")

import os
def Search_HourseOf(Worker):
    for item in ListHourseOf:
        if (item["Имя"] == Worker["Имя"] and item["Фамилия"] == Worker["Фамилия"]):
            return item
def Calculate_ZP(Stavka, Norma, Otrabotano):
    StoimostChasa = Stavka / Norma
    if Otrabotano > Norma:
        Pererabotka = Otrabotano - Norma
        return(Stavka+Pererabotka*2*StoimostChasa)
    elif Otrabotano < Norma:
        Nedorabotka = Norma - Otrabotano
        return(Stavka-Nedorabotka*StoimostChasa)
    else:
        return(Stavka)


def Parcing_file(DIR, FileName):
    List_Data = []
    with open(os.path.join(DIR, FileName), 'r', encoding='UTF-8') as f:
        for i, line in enumerate(f):  # считываем файл построчно
            #Первую строку парсим как заголовок
            if i == 0:
                header = line.split()
            else:
                #Все остальные строки парсим с данными
                d ={}
                data_line = line.split()
                for j, item in enumerate(header):
                    if j < len(data_line):
                        d[item] = data_line[j]
                    else:
                        d[item] = ""
                List_Data.append(d)
    return List_Data



DIR = "data"
FileName_Workers = "workers"
FileName_HourseOf = "hours_of"
ListWorkers = Parcing_file(DIR,FileName_Workers)
# print(ListWorkers)
ListHourseOf = Parcing_file(DIR,FileName_HourseOf)
# print(ListHourseOf)
print("Начислено ЗП:")
for Worker in ListWorkers:
    Otrabotano = float(Search_HourseOf(Worker)["Отработано_часов"])
    Norma = float(Worker["Норма_часов"])
    Stavka = float(Worker["Зарплата"])
    print(Worker["Фамилия"], Worker["Имя"], round(Calculate_ZP(Stavka, Norma, Otrabotano),2))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("\nЗадание-3")

def Parcing_file(DIR, FileName):
    List_Data = []
    with open(os.path.join(DIR, FileName), 'r', encoding='UTF-8') as f:
        for line in f:  # считываем файл построчно
            if line != "\n":
                List_Data.append(line.replace("\n",""))
    return List_Data

def WriteFile(NameFruit):
    FileName = "fruits_"+NameFruit[0]
    with open(os.path.join(DIR, FileName), 'a', encoding='UTF-8') as f:
        f.writelines(NameFruit+"\n")


DIR = "data"
FileName_fruits = "fruits.txt"
Listfruits = Parcing_file(DIR, FileName_fruits)
for fruit in Listfruits:
    WriteFile(fruit)
print("Выполнено")



