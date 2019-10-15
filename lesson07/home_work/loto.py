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
        self.vsego_bochenok = 90
        self._list_bochenok = [i for i in range(1,self.vsego_bochenok+1)]
    def get_bochenok(self):
        if self.get_ostalos() > 0:
            import random
            number = random.randint(1, len(self._list_bochenok))
            bochenok = self._list_bochenok[number-1]
            self._list_bochenok.remove(bochenok)
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
    def draw(self):
        prefix = '-' * int((24-len(self.name))/2)
        sufix = "-" * (28 - len(self.name)-len(prefix) - 4)
        print(prefix,self.name,sufix)
        for i in range(3):
            l = [str(x) for x in self._matrix_3x9[i]]
            print((', '.join([x if len(x) != 1 else " "+x for x in l]).replace(',', '').replace(' 0', '  ')))
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
    def Output(self):
        print("Новый бочонок: {0} (осталось {1})".format(self.Meshok_.get_bochenok(), self.Meshok_.get_ostalos()))
        self.Kartochka_Computer_.draw()
        self.Kartochka_Gamer_.draw()
        print("Зачеркнуть цифру? (y/n)")
    def run(self):
        self.Output()




Game_ = Game()
Game_.run()


