# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

print("Задание-1")

class sotrudnik():
    def __init__(self,header,init_str):
        data_line = init_str.split()
        for j, item in enumerate(header):
            if j < len(data_line):
                setattr(self,item,data_line[j])
class vedomost():
    def __init__(self):
        self.list_sotrudnik = []
        self.list_hours_of = []
        self.__init_sprav_sotrudnik()
        self.__init_otrabotka()
    def __init_sprav_sotrudnik(self):
        import os
        DIR = "data"
        FileName = "workers"
        with open(os.path.join(DIR, FileName), 'r', encoding='UTF-8') as f:
            for i, line in enumerate(f):  # считываем файл построчно
                # Первую строку парсим как заголовок
                if i == 0:
                    header = line.split()
                else:
                    # Все остальные строки с данными
                    # Создаем экзэмпляр класса сотрудник и добавляем в справочник сотрудников
                    self.list_sotrudnik.append(sotrudnik(header,line))
    def get_sotrudmik(self,name,family_name):
        for item in self.list_sotrudnik:
            if item.Имя == name and item.Фамилия == family_name:
                return item
    def __init_otrabotka(self):
        def add_hours_of(self, header, init_str):
            d = {}
            data_line = init_str.split()
            for j, item in enumerate(header):
                if j < len(data_line):
                     d[item] = data_line[j]
                else:
                     d[item] = ""
            sotrudnik = self.get_sotrudmik(d["Имя"], d["Фамилия"])
            setattr(sotrudnik, item, d["Отработано_часов"])
        import os
        DIR = "data"
        FileName = "hours_of"
        with open(os.path.join(DIR, FileName), 'r', encoding='UTF-8') as f:
            for i, line in enumerate(f):  # считываем файл построчно
                # Первую строку парсим как заголовок
                if i == 0:
                    header = line.split()
                else:
                    # Все остальные строки с данными
                    # Добавляем атрибут отработки сотруднику
                    add_hours_of(self, header, line)
    def Calculate_ZP(self):
        for item in self.list_sotrudnik:
            StoimostChasa = int(item.Зарплата) / int(item.Норма_часов)
            if int(item.Отработано_часов) > int(item.Норма_часов):
                Pererabotka = int(item.Отработано_часов) - int(item.Норма_часов)
                setattr(item, "Начислено", int(item.Зарплата)+Pererabotka*2*StoimostChasa)
            elif int(item.Отработано_часов) < int(item.Норма_часов):
                Nedorabotka = int(item.Норма_часов) - int(item.Отработано_часов)
                setattr(item, "Начислено", int(item.Зарплата)-Nedorabotka*StoimostChasa)
            else:
                setattr(item, "Начислено", item.Зарплата)
            print("Имя: {} Фамилия: {} Зарплата: {} Начислено: {}".format(item.Имя,item.Фамилия,item.Зарплата,item.Начислено))

vedomost = vedomost()
vedomost.Calculate_ZP()