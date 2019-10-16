#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

class Meshok():
    def __init__(self):
        self.current_bochenok = None
        self.vsego_bochenok = 90
        self._list_bochenok = [i for i in range(1,self.vsego_bochenok+1)]
    def get_bochenok(self):
        if self.get_ostalos() > 0:
            import random
            number = random.randint(1, len(self._list_bochenok))
            bochenok = self._list_bochenok[number-1]
            self._list_bochenok.remove(bochenok)
            self.current_bochenok = bochenok
            return bochenok
        else:
            print("Мешок пуст")
    def get_ostalos(self):
        return len(self._list_bochenok)

class Kartochka():
    def __init__(self,name,vsego_bochenok):
        self.vsego_bochenok = vsego_bochenok
        self.name = name
        self._matrix_3x9 = []
        self.fill_matrix_3x9()
    def fill_matrix_3x9(self):
        import random
        for i in range(3):
            self._matrix_3x9.append([0 for x in range(9)])
            list_number = sorted(random.sample(range(self.vsego_bochenok+1),5))
            for inx,x in enumerate(sorted(random.sample(range(1,10),5))):
                self._matrix_3x9[i][x-1] = list_number[inx]
    def close_cell(self,listcell):
        for cell in listcell:
            self._matrix_3x9[cell[0]][cell[1]] = -1
    def get_List_closecell(self,current_bochenok):
        Res = []
        for inx,row in enumerate(self._matrix_3x9):
            try:
                col = row.index(current_bochenok)
                Res.append((inx,col))
            except Exception:
                pass
        return Res
    def verify_end(self):
        L = []
        for item in self._matrix_3x9:
            L += [x for x in item if x > 0 ]
        return len(L) == 0
    def draw(self):
        prefix = '-' * int((24-len(self.name))/2)
        sufix = "-" * (28 - len(self.name)-len(prefix) - 4)
        print(prefix,self.name,sufix)
        for i in range(3):
            l = [str(x) for x in self._matrix_3x9[i]]
            print((', '.join([x if len(x) != 1 else " "+x for x in l]).replace(',', '').replace(' 0', '  ').replace('-1', ' -')))
        print('-'*26)
            #print(self._matrix_3x9[i])
            #print([len(x) for x in l])

class Kartochka_Computer(Kartochka):
    def __init__(self,vsego_bochenok):
        self.name = "Карточка компьютера"
        super().__init__(self.name,vsego_bochenok)

class Kartochka_Gamer(Kartochka):
    def __init__(self,vsego_bochenok):
        self.name = "Карточка игрока"
        super().__init__(self.name,vsego_bochenok)

class Game():
    def __init__(self):
        self.Meshok_ = Meshok()
        self.Kartochka_Computer_ = Kartochka_Computer(self.Meshok_.vsego_bochenok)
        self.Kartochka_Gamer_ = Kartochka_Gamer(self.Meshok_.vsego_bochenok)
    def output(self):
        print('\n' * 80)
        print("Новый бочонок: {0} (осталось {1})".format(self.Meshok_.current_bochenok, self.Meshok_.get_ostalos()))
        self.Kartochka_Computer_.draw()
        self.Kartochka_Gamer_.draw()
    def input_gamer(self):
        while True:
            request = input("Зачеркнуть цифру? (y/n)\n>>")
            if request in ["y","Y"]:
                break
            elif request in ["n","N"]:
                return "Skip"
            self.output()
        while True:
            try:
                resp_str = input("Введите номера позиций на карточке в формате (i1,j1), (i2,j2), ... - где i1-номер строки, "
                                "j1 - номер столбца в карточке. Номера начинаются с 1 \n>>")
                #Преобразуем введенную строку в список кортежей, где кортеж - координаты поля
                s = resp_str[1:][:-1].split("),(")
                resp = [tuple([int(y)-1 for y in x.split(",")]) for x in s]
                return resp
            except Exception as e:
                print("Ошибка ввода, для продолжения нажмите Enter.\n",e)
                input()
            self.output()


    def verify_end(self):
        res_comp = self.Kartochka_Computer_.verify_end()
        res_gamer = self.Kartochka_Gamer_.verify_end()
        if res_comp and res_gamer:
            print("У вас ничья. Игра окончена")
            exit()
        elif res_comp:
            print("Вы проиграли, ваш аппонент закрыл карточку нраньше вас")
            exit()
        elif res_gamer:
            print("Поздравляем, вы победили")
            exit()

    def run(self):
        while True:
            self.verify_end()
            self.Meshok_.get_bochenok()
            list_closecell_computer = self.Kartochka_Computer_.get_List_closecell(self.Meshok_.current_bochenok)
            self.Kartochka_Computer_.close_cell(list_closecell_computer)
            self.output()
            list_closecell_gamer = self.input_gamer()
            true_list_closecell_gamer = self.Kartochka_Gamer_.get_List_closecell(self.Meshok_.current_bochenok)
            if list_closecell_gamer == "Skip":
                #если пользователь пропустил ход, то проверяем что правильных ответов действительно нет
                if len(true_list_closecell_gamer) == 0:
                    continue
                else:
                    self.output()
                    print("К сожлению вы произрали. Правильный ответ:\n",true_list_closecell_gamer)
                    exit()
            else:
                #если пользователь ввел ячейки, то проверяем, что его ответ правильный
                if sorted(true_list_closecell_gamer) == sorted(list_closecell_gamer):
                    self.Kartochka_Gamer_.close_cell(list_closecell_gamer)
                else:
                    self.output()
                    if len(true_list_closecell_gamer) == 0:
                        print("К сожлению вы произрали. Такого номера боченка не было на вашей карточке")
                    else:
                        print("К сожлению вы произрали. Правильный ответ:\n",[(item[0]+1,item[1]+1) for item in true_list_closecell_gamer])
                    exit()

            #input("Введите Enter чтобы продолжить")


Game_ = Game()
Game_.run()


