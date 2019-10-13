# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

print("Задание-1")

class klass():
    def __init__(self,name):
        self.name
class uchenik():
    def __init__(self,name,klass,fio_mama,fio_papa):
        self.name = name
        self.klass = klass
        self.fio_mama = fio_mama
        self.fio_papa = fio_papa
class teacher():
    def __init__(self,name,predmet,list_klass):
        self.name = name
        self.predmet = predmet
        self.list_klass = list_klass

class school():
    def __init__(self,name):
        self.name = name
        self.list_uchenik = []
        self.list_teacher = []
    def add_uchenik(self,uchenik):
        self.list_uchenik.append(uchenik)
    def add_teacher(self, teacher):
        self.list_teacher.append(teacher)
    def get_listklass(self):
        l = list(set([uchenik.klass for uchenik in self.list_uchenik]))
        return l
    def get_listuchenik(self,klass):
        l = [uchenik.name for uchenik in self.list_uchenik if uchenik.klass == klass]
        return l
    def get_listpredmet(self,fio_uchenik):
        u = ""
        for uchenik in self.list_uchenik:
            if uchenik.name == fio_uchenik:
                u = uchenik
                break
        if not u:
            return "Ученик с таким ФИО не найден"
        print(u.klass)
        res = []
        for teacher in self.list_teacher:
            if u.klass in teacher.list_klass:
                res.append("Ученик: {} Класс: {} Преподаватель: {} Предмет: {}".format(u.name,u.klass,teacher.name,teacher.predmet))
        return res
    def get_roditeli(self,fio_uchenik):
        for uchenik in self.list_uchenik:
            if uchenik.name == fio_uchenik:
                return "Отец: {} Мать: {}".format(uchenik.fio_papa,uchenik.fio_mama)
    def get_teacher(self,klass):
        l = [teacher.name for teacher in self.list_teacher if klass in teacher.list_klass]
        return l

school = school("Школа 1111")
school.add_uchenik(uchenik("Иванов Василий Алибабаевич","5А","Иванова Ирина Васильевна","Иванов Павел Петрович"))
school.add_uchenik(uchenik("Сидорова Елена Олеговна","5А","Сидорова Полина Васильевна","Сидоров Егор Александрович"))
school.add_uchenik(uchenik("Петрова Анна Александровна","7Б","Петрова Виктория Тимофеевна","Петров Сергей Сергеевич"))
school.add_uchenik(uchenik("Синичкина Ольга Петровна","7Б","Синичкина Татьяна Егоровна","Синичкин Иван Алексеевич"))
school.add_uchenik(uchenik("Козлова Анна Денисовна","3Б","Петрова Виктория Тимофеевна","Петров Сергей Сергеевич"))
school.add_uchenik(uchenik("Щукина Виктория Максимовна","3Б","Синичкина Татьяна Егоровна","Синичкин Иван Алексеевич"))
school.add_teacher(teacher("Федоров Иван Иванович","Математика",["5А","7Б","3Б"]))
school.add_teacher(teacher("Павлов Сергей Генадьевич","Физкультура",["5А","7Б","3Б"]))

#Получаем список учеников в классе
print(school.get_listuchenik("3Б"))
#Получаем список всех классов
print(school.get_listklass())
#Получаем список всех предметов у ученика
print(school.get_listpredmet("Щукина Виктория Максимовна"))
#Получаем родителей ученика
print(school.get_roditeli("Щукина Виктория Максимовна"))
#Получаем список учителей в классе
print(school.get_teacher("3Б"))
