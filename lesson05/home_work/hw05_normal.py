# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
def action1():
    'Перейти в папку'
    InpStr = input("Введите название папки\n")
    os.chdir(os.path.join(os.getcwd(), InpStr))
    print("Текущая папка: {}".format(os.path.basename(os.getcwd())))

def action2():
    'Просмотреть содержимое текущей папки'
    print("Cодержимое текущей папки:")
    [print(item) for item in os.listdir(os.getcwd())]

def action3():
    'Удалить папку'
    InpStr = input("Введите название папки\n")
    try:
        os.rmdir(os.path.join(os.getcwd(), InpStr))
        print("Успешное удаление папки: {}".format(InpStr))
    except FileExistsError:
        print("Не найдена папка: {}".format(InpStr))



def action4():
    'Создать папку'
    InpStr = input("Введите название папки\n")
    try:
        os.mkdir(os.path.join(os.getcwd(), InpStr))
        print("Успешное создание папки: {}".format(InpStr))
    except:
        print("Папка не создана: {}".format(InpStr))

Dict ={"1": action1, "2": action2, "3": action3, "4": action4}
InpStr = ""
while True:
    os.system('cls')
    InpStr = input("1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\nq. Выход\n\nСделайте выбор:\n")
    if InpStr == "q":
        exit()
    #print(dict)
    if InpStr in Dict:
        Dict[InpStr]()
    else:
        print("Неверный выбор\n")
    input("\nНажмите Enter чтобы продолжить\n")




