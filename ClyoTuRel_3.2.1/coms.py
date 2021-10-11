from math import *

from graph import *


class Empire:
    AllEmpires = []  # глобальный массив всех империй с объектами Empire

    number = sqrt(0)  # порядковый номер империи
    old = []  # массив с объектами Field, массив земель империии
    LandsQuantity = 0  # A, количество земель империи
    Asabia = 0.0  # S , асабия средняя
    center_x = -1  # х - координата центра масс империи
    center_y = -1  # у - координата центра масс империии
    S_critical = 0.03  # критическое значение асабии, при котором империя разваливается
    EmpiresQ = []  # глобальный массив с кол-вом империй

    def __init__(self, n, eq, Scr, *args):  # аргс -- несколько подряд идущих филдов, принадлежащих империи
        self.S_critical = Scr  # то есть земли, при объявлении мперии принадлежащие ей
        self.EmpiresQ = eq
        self.old = []
        self.number = self.EmpiresQ[0]

        self.EmpiresQ[0] += 1

        for i in args:
            self.old.append(i)  # добавление филдов в массив земель
            if n != -1:
                i.Asabia = n  # присвоение имперским клеткам имперской асабии

        self.LandsQuantity = len(self.old)
        self.centers()  # вычисление центра масс
        self.AllEmpires = self.old[0].AllEmpires  # присвоение глобального массива по ссылке на
        # глобальный массив от одного из филдов

        for i in self.old:  # говорим филду, что он принадлежит    ЭТОЙ империи
            i.Empire = self

    def pre_update(self):
        self.LandsQuantity = len(self.old)  # обновление кол-ва земель в империи

    def update(self):
        if self.LandsQuantity >= 2:  # если в импертии больше 2 земель
            self.Asabia = sum([i.Asabia for i in self.old]) / self.LandsQuantity
            self.centers()

            if self.Asabia < self.S_critical:  # если асабия меньше критической, то хуй вам, а не империя
                self.die()  # TONIGHT WE'LL DINE IN HELL
        else:
            self.die()

    def centers(self):  # подсчёт координаты центра масс империи
        self.center_x, self.center_y = 0, 0
        for i in self.old:
            self.center_x += i.x
            self.center_y += i.y

        if len(self.old) != 0:
            self.center_x /= len(self.old)
            self.center_y /= len(self.old)
        else:
            self.center_y, self.center_x = -1, -1

    def die(self):  # "смерть" империи
        for i in self.old:  # объявление её земель ничейными
            i.Empire = 'None'
            i.Borders = 'Border'
        if self in self.AllEmpires:  # удаление её из массива всех империй (он глобальный)
            del self.AllEmpires[self.AllEmpires.index(self)]

    def __str__(self):  # то, как выводится объект Империя, т.е.
        s = ''  # координаты её земель . так, самая перва империя выведется так:
        for i in self.old:  # 0 0  1 0  0 1  1 1
            s += str(i.x) + ' ' + str(i.y) + '  '

        return s + '\n'


class Field:  # класс филдов/полей/провок/клеток
    BigMapP = []  # глобальный двумерный массив, содержащий все филды
    AllEmpires = []  # глобальный двумерный маасив, содержащий все империи

    chance = 50  # 1/ вероятность возникновения варварской империи при удачной атаке
    Asabia = 0.0  # стартовая асабия
    Borders = 'Border'  # показатель, нахожится клетка на границе или в центре
    Empire = 'None'  # показатель, к какой империи она относится: либо None, либо номер империи, либо Landscape
    x = 0  # х - координата клетки
    y = 0  # у - координата клетки
    # т.е. в том массиве эта клетка -- это BigMapP[y][x] , да именно так
    status = 'old_fag'  # ньюфаг только если захвачена в этом ходу, т.е.

    # чтобы только что захваченная клетка не могла атаковать

    def __init__(self, r, dd, ass, h, dp, length, width, x, y, ch):
        self.Asabia = ass  # ну тут ввод всего + констант из турчина
        self.chance = ch
        self.r0 = r
        self.d = dd
        self.x = h
        self.x = x
        self.y = y
        self.dp = dp
        self.length = length  # это длина карты, то есть по иксу
        self.width = width  # это по игреку

    def pre_update(self):

        # if self.Empire != 'None':
        if self.Empire != 'Landscape':
            if self.Empire != 'None' and (self.x == 0 or self.y == 0 or self.y == self.width - 1 or self.x == self.length - 1):
                self.Borders = 'Border'  # это по кд не выполняется # пиздишь, сука
            else:
                q = False  # это штука, говорящая, что если мы хотьь раз решили, что филд
                # на границе, то он рили на границе
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if q:
                            break
                        if abs(i) + abs(j) < 2:  # здесь перебираем всех соседей сверху снизу слева справа (4 штуки)
                            if 0 <= self.y + i < self.width and 0 <= self.x + j < self.length:  # проверяем,не будет ли индекс невозможным для массива
                                if str(self.BigMapP[self.y + i][self.x + j].Empire) != str(
                                        self.Empire) and \
                                        self.BigMapP[self.y + i][
                                            self.x + j].Empire != 'Landscape':  # если 1 из соседов этой клетки
                                    self.Borders = 'Border'  # принадлежит другой империи (или ничей), то она на границе
                                    q = True  # тогда других соседов проверять нет смысла
                                    break
                                else:
                                    self.Borders = 'Center'  # а если других империй рядом нет, то клетка в центре
                    if q:
                        break
        else:
            self.Borders = 'Center'

        self.status = 'old_fag'  # т.к. в цикле у меня идёт сначала апдейты, потом атака
        # то при апдейте можно говоить клетке, что она уже олфаг

    def update(self):  # в зависимости от нахождения в центре/на границе
        # по турчину считаем асабию

        # if self.Empire != 'None':
        if self.Empire != 'Landscape':
            if self.Borders == 'Border':
                self.Asabia += self.r0 * self.Asabia * (1 - self.Asabia)
            elif self.Borders == 'Center' and self.Empire != 'None':
                self.Asabia -= self.d * self.Asabia

        if self.Asabia < 0.000001:
            self.Asabia = 0.000001
        elif self.Asabia > 0.999999:
            self.Asabia = 0.999999

    def __str__(self):  # формат вывода: два символа, отвечающие за империю, пробел,
        # один символ, отвечающий за нахождение на границе/центре, 4 символа, отвечающие
        # за асабию, пробел. Ну и в начале/конце символ | помогающий отделиить клетки друг
        # от друга. Пример вывода для клеток
        #  империя 34, Center, асабия 0.67:     | 34 С0.67
        # враварская клетка (империя None), Border, асабия 0.78: | ne B0.78
        if self.Empire == 'None' or self.Empire == 'Landscape':
            s = '| ' \
                + str(self.Empire) \
                + ' ' + str(str(round(self.Asabia, 2))
                            + '0' * (4 - len(str(round(self.Asabia, 2))))) \
                + ' ' + str(self.Borders[0])
        else:
            s = '| ' \
                + str('0' * (4 - len(str(self.Empire.number)))
                      + str(self.Empire.number)) \
                + ' ' + str(str(round(self.Asabia, 2))
                            + '0' * (4 - len(str(round(self.Asabia, 2))))) \
                + ' ' + str(self.Borders[0])

        return s[:2] + s[4:7] + s[12] + s[7:11]

    def attack(self, field):  # функция атаки филдом другого филда field
        if self.Empire != field.Empire or self.Empire == 'None':
            # атака возможна только если филды разных империй или один из них нон
            if self.Empire == 'None':  # считаемм мощь атакующего филда
                p1 = 1 * self.Asabia * e ** (0)
            else:
                p1 = self.Empire.LandsQuantity * self.Empire.Asabia * \
                     e ** (- distance(self.Empire.center_x, self.Empire.center_y,
                                      self.x, self.y))

            if field.Empire == 'None':  # считаем мощь атакуемого филда
                p2 = 1 * field.Asabia * e ** (0)
            else:
                p2 = field.Empire.LandsQuantity * field.Empire.Asabia * \
                     e ** (- distance(field.Empire.center_x, field.Empire.center_y,
                                      field.x, field.y))

            if self.dp < p1 - p2:  # если мощь атакующего на нужное число больше мощи атакуемого
                # то атака успешnа
                if self.Empire != 'None':  # если атакующий -- имперский
                    Emp = field.Empire
                    if Emp != 'None':  # если атакуемый -- имперский
                        if field in Emp.old:
                            del Emp.old[Emp.old.index(field)]  # удаляме его из массива земель его империи
                    field.Empire = self.Empire  # говорим, что его империя -- империя нашего филда
                    field.Asabia = (self.Asabia + field.Asabia) / 2  # асабия считается по турчину
                    field.status = 'new_fag'  # завоёван в этот ход, то есть ньюфаг
                    self.Empire.old.append(field)  # добпаляем в массив нашей империи его

                else:  # если атакующий -- нон
                    if randrange(self.chance) == 0:  # учитывваем шанс создания империи
                        Emp = field.Empire  # (по дефолту он 1)
                        if Emp != 'None':  # ну тут аналогично
                            if field in Emp.old:
                                del Emp.old[Emp.old.index(field)]
                        self.AllEmpires.append(Empire(-1, self.AllEmpires[0].EmpiresQ,
                                                      self.AllEmpires[0].S_critical,
                                                      self,
                                                      field))  # тк атакующий-неимперский победил, создаём ему империю
                        field.Asabia = (self.Asabia + field.Asabia) / 2  # ну и по турчину считаем асабию
                        field.status = 'new_fag'
