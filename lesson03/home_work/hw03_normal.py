# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n, m):
    R = []
    for i in range(n,m):
        R.append(fib(i))
    return R

print(fibonacci(0, 11))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(i+1,len(origin_list)):
            if origin_list[i] > origin_list[j]:
                temp_= origin_list[i]
                origin_list[i] = origin_list[j]
                origin_list[j] = temp_
    return origin_list
            #print(i,j)
            # print(origin_list[i])


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(fun,l):
    R = []
    for Item in l:
        if fun(Item):
            R.append(Item)
    return  R

#пределяем исходный список и лямбда функцию
l = [5, 9, 5, 3, 2, 8, 10]
fun = lambda x: x > 6

print(my_filter(fun, l))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

P1 = {"x":1,"y":1}
P2 = {"x":2,"y":4}
P3 = {"x":6,"y":4}
P4 = {"x":5,"y":1}

def Vetify_Parallel(Para1,Para2):
    if (Para1[1].get("x") != Para1[0].get("x")):
        A1= (Para1[1].get("y")-Para1[0].get("y"))/(Para1[1].get("x")-Para1[0].get("x"))
    else:
        A1 = 0
    if (Para2[1].get("x") != Para2[0].get("x")):
        A2= (Para2[1].get("y")-Para2[0].get("y"))/(Para2[1].get("x")-Para2[0].get("x"))
    else:
        A2 = 0
    if A1 == A2:
        return True
    else:
        return False

#Выясняем параллельны ли противоположные стороны у четырехугольника
Para1 = (P1,P2)
Para2 = (P3,P4)
if not Vetify_Parallel(Para1,Para2):
    Para1 = (P2,P3)
    Para2 = (P1,P4)
    if not Vetify_Parallel(Para1,Para2):
        print("У четырехугольника стороны не параллельны - это не параллограмм")
        exit()
print("Это параллелограмм")