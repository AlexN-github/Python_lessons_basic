# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

print("Задача-1")

class triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calculate_area(self):
        r = 0.5*abs((p2["x"]-p1["x"])*(p3["y"]-p1["y"]) - (p3["x"]-p1["x"])*(p2["y"])-p1["y"])
        return r

    def calculate_heights(self):
        def get_height(p1,p2,p3):
            import math
            distance = abs((p3["y"]-p2["y"])*p1["x"]-(p3["x"]-p2["x"])*p1["y"]+p3["x"]*p2["y"]-p3["y"]*p2["x"])/math.sqrt((p3["y"]-p2["y"])**2 + (p3["x"]-p2["x"])**2)
            return distance
        h1 = get_height(self.p1, self.p2, self.p3)
        h2 = get_height(self.p2, self.p3, self.p1)
        h3 = get_height(self.p3, self.p1, self.p2)
        return h1,h2,h3

    def calculate_perimeter(self):
        def get_len(p1,p2):
            import math
            len = math.sqrt((self.p2["x"] - self.p1["x"]) ** 2 + (self.p2["y"] - self.p1["y"]) ** 2)
            return len

        p1p2 = get_len(p1,p2)
        p2p3 = get_len(p2,p3)
        p3p1 = get_len(p3,p1)
        perimeter = p1p2+p2p3+p3p1
        return perimeter

p1 = {"x": 5,
      "y": 7}
p2 = {"x": 3,
      "y": 4}
p3 = {"x": 6,
      "y": 1}
tr = triangle(p1,p2,p3)
print("Площадь:", tr.calculate_area())
print("h1,h2,h3", tr.calculate_heights())
print("Периметр:", tr.calculate_perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print("Задача-2")

class ravtrapetc:
    def __get_abc(self):
        def get_len(p1, p2):
            import math
            len = math.sqrt((self.p2["x"] - self.p1["x"]) ** 2 + (self.p2["y"] - self.p1["y"]) ** 2)
            return len
        self.C = get_len(self.p1,self.p2)
        self.B = get_len(self.p2,self.p3)
        self.A = get_len(self.p4,self.p1)


    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.__get_abc()
    def verify(self):
        'Если стороны A и B параллельны, а углы сторон C с онованием трапеции равны'
        def Vetify_Parallel(self):
            if self.p1["x"] != self.p4["x"]:
                A1 = (self.p1["y"] - self.p4["y"]) / (self.p1["x"] - self.p4["x"])
            else:
                A1 = 0
            if self.p2["x"] != self.p3["x"]:
                A2 = (self.p2["y"] - self.p3["y"]) / (self.p2["x"] - self.p3["x"])
            else:
                A2 = 0
            if A1 == A2:
                return True
            else:
                return False
        def Vetify_equality_angles(self):
            import math
            angles1 = (((self.p1["x"]-self.p2["x"])**2)+((self.p1["y"]-self.p2["y"])**2)+((self.p1["x"]-self.p4["x"])**2)+((self.p1["y"]-self.p4["y"])**2)-((self.p2["x"]-self.p4["x"])**2)-((self.p2["y"]-self.p4["y"])**2))/(2*math.sqrt(((self.p1["x"]-self.p2["x"])**2)+((self.p1["y"]-self.p2["y"])**2))*math.sqrt(((self.p1["x"]-self.p4["x"])**2)+((self.p1["y"]-self.p4["y"])**2)))
            angles2 = (((self.p4["x"]-self.p3["x"])**2)+((self.p4["y"]-self.p3["y"])**2)+((self.p4["x"]-self.p1["x"])**2)+((self.p4["y"]-self.p1["y"])**2)-((self.p3["x"]-self.p1["x"])**2)-((self.p3["y"]-self.p1["y"])**2))/(2*math.sqrt(((self.p4["x"]-self.p3["x"])**2)+((self.p4["y"]-self.p3["y"])**2))*math.sqrt(((self.p4["x"]-self.p1["x"])**2)+((self.p4["y"]-self.p1["y"])**2)))
            if angles1 == angles2:
                return True
            else:
                return False

        if Vetify_Parallel(self) and Vetify_equality_angles(self):
            return True




    def calculate_perimeter(self):
        perimeter = self.A+self.B+2*self.C
        return perimeter
    def calculate_area(self):
        import math
        area = (self.A+self.B)/2*math.sqrt(self.C**2 - (self.A-self.B)**2/4)
        return area

p1 = {"x": 1,
      "y": 1}
p2 = {"x": 2,
      "y": 7}
p3 = {"x": 7,
      "y": 7}
p4 = {"x": 8,
      "y": 1}



trap = ravtrapetc(p1,p2,p3,p4)
print("Это равнобедренная тропеция?:", trap.verify())
print("Площадь:", trap.calculate_area())
print("Стороны: A= {}, B= {}, C= {}".format(trap.A, trap.B, trap.C))
print("Периметр:", trap.calculate_perimeter())

