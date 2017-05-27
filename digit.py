# -*- coding: utf-8 -*-
"""
modul digit
author: decard
22.05.17
"""


def rolltime(self_t, self_z):
    """
    self_t - список времени
    self_z - список к тому к чему привязываемся, пока настроенно на 1
    приводим шкалу времени разных сигналов  к началу 0 от которого
    будем сравнивать
    """
    if self_z[0] == 0:
        for i in self_z:
            a = self_z.index(1)
    elif self_z[0] == 1:
        return(self_t)
    b = []
    for i in self_t:
        z = i - self_t[a]
        b.append(z)
    return b


def searchpoint(self, time):
    """
    Ищет точки екстренума
    на выходе имееем список
    [[t0, t1, 0, 1], [t1, t0, 1, 0], ...]
    так сказать снимаем дамп сигнала
    """
    c = []
    b1 = [0, 1]
    b2 = [1, 0]
    for i in range(len(self)):
        chunk = self[i:i + 2]
        if b1 == chunk:
            a = time[i:i + 2]
            b = self[i:i + 2]
            c1 = a + b
            c.append(c1)
        if b2 == chunk:
            a = time[i:i + 2]
            b = self[i:i + 2]
            c2 = a + b
            c.append(c2)
    return c


def compare(self, data, BORDER=1):
    """
    сравнение двух сигалов значения беруться из дампов
    BORDER число дельта сравниваем сигналы входит в ли диапазон
    """
    print('Сравниваю...')
    for i, o in zip(self, data):
        if i[3] and o[3] == 1:
            delta = i[1] - o[1]
            if abs(delta) < BORDER:
                print(delta, 'good')
            else:
                print(delta, 'bed')
        elif i[2] and o[2] == 1:
            delta = i[0] - o[0]
            if abs(delta) < BORDER:
                print(delta, 'good')
            else:
                print(delta, 'bed')
        else:
            print('Не та последовательность сигналов')
