# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil

#print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not Second_param:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), Second_param)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(Second_param))
    except Exception as err:
        print(err)



def ping():
    print("pong")

def cp():
    'создает копию указанного файла'
    if not Second_param:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copy(os.path.join(os.getcwd(), Second_param), os.path.join(os.getcwd(), Second_param)+".Copy")
        print("Файл успешно скопирован: {}".format(Second_param))
    except Exception as err:
        print(err)


def rm():
    'удаляет указанный файл'
    if not Second_param:
        print("Необходимо указать имя файла вторым параметром")
        return
    while True:
        Res = input("Вы действительно хотите удалить файл {} (y/n)\n".format(Second_param))
        if Res in ["y", "Y"]:
            break
        if Res in ["n", "N"]:
            exit()
    try:
        os.remove(os.path.join(os.getcwd(), Second_param))
        print("Успешное удаление файла: {}".format(Second_param))
    except Exception as err:
        print(err)

def cd():
    'меняет текущую директорию на указанную'
    if not Second_param:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(os.path.join(os.getcwd(), Second_param))
        print("Текущая папка: {}".format(os.path.basename(os.getcwd())))
    except Exception as err:
        print(err)


def ls():
    'отображение полного пути текущей директории'
    try:
        print("Текущая папка:")
        print(os.path.basename(os.getcwd()))
    except Exception as err:
        print(err)

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    Second_param = sys.argv[2]
except IndexError:
    Second_param = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
else:
    print("Задан неверный ключ")
    print("Укажите ключ help для получения справки")
