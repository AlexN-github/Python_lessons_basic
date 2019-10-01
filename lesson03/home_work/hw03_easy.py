# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    if number*10**ndigits % 1 >= 0.5:
        res = (int((number*10**ndigits)) +1) / 10**ndigits
    else:
        res = int((number*10**ndigits)) / 10**ndigits
    return res



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#test branch

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Функция суммирования чисел в строке
def sum_number_str(number_str):
    sum = 0
    for num in list(number_str):
        sum += int(num)
    return sum
def lucky_ticket(ticket_number):
    StartFirst = 0
    if len(str(ticket_number)) / 2 % 1 == 0:
        # Если четное количество цифр, то количетсво цифр делим пополам
        StopFirst = int(len(str(ticket_number)) / 2)
        StartSecond = StopFirst
    else:
        # Если нечетное, то среднюю цифру не считаем ни первой не последней
        StopFirst = int(len(str(ticket_number)) / 2)
        StartSecond = StopFirst + 1
    StopSecond = StartSecond+StopFirst
    #print(StartFirst,StopFirst,StartSecond,StopSecond)
    ticket_number_S = str(ticket_number)
    First = ticket_number_S[StartFirst:StopFirst]
    Second = ticket_number_S[StartSecond:StopSecond]
    if sum_number_str(list(First)) == sum_number_str(list(Second)):
        Res = "lucky"
    else:
        Res = "Unlucky"
    return Res



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
