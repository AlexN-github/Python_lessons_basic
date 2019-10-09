# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создаем новую директорию
print("Задача-1")

print("Создаем директории dir_1..dir_9")
import os
current_path = os.getcwd()
try:
    for i in range(1,10):
        FullNameDir = os.path.join(current_path, "dir_"+str(i))
        os.mkdir(FullNameDir)
    print("Директории dir_1..dir_2 созданы")
except FileExistsError:
    print('Директория {} уже существует'.format("dir_"+str(i)))

print("Удаляем директории dir_1..dir_9")
import os
current_path = os.getcwd()
try:
    for i in range(1,10):
        FullNameDir = os.path.join(current_path, "dir_"+str(i))
        if os.path.isdir(FullNameDir):
            os.rmdir(FullNameDir)
    print("Директории dir_1..dir_2 удалены")
except :
    print('Ошибка при удалении директории {}'.format("dir_"+str(i)))

#exit()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print("Задача-2")

import os
print([item for item in os.listdir(os.getcwd()) if os.path.isdir(item)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil
ScriptPath = sys.argv[0]
CopyScriptPath = ScriptPath+"_copy"
print(ScriptPath)
print(ScriptPath+"_copy")

shutil.copy(ScriptPath, CopyScriptPath)