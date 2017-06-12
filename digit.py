# -*- coding: utf-8 -*-

"""
modul digit
author: decard
22.05.17
"""

import decimal


def rolltime(UpPointList, TimeList):
    """
    :type UpPointList: список относительно которого будем сдвигать время, сдвигаем от первого вхождения '1'
    :type TimeList: список временных отметок]
    """
    decimal.getcontext().prec = 15
    if UpPointList[0] == 0:
        idnex = UpPointList.index(1)
    elif UpPointList[0] == 1:
        return TimeList
    NewTime = []
    for i in TimeList:
        PointTime = decimal.Decimal(i) - decimal.Decimal(TimeList[idnex])
        NewTime.append(PointTime)
    return NewTime


def searchpoint(PointList, TimeList):
    """
    Ищем точки экстренума, на выходе имееем список
    [[t0, t1, 0, 1], [t1, t0, 1, 0], ...]
    снимаем дамп сигнала
    """
    dump = []
    high = [0, 1]
    down = [1, 0]
    for i in range(len(PointList)):
        chunk = PointList[i:i + 2]
        if high == chunk:
            time = TimeList[i:i + 2]
            point = PointList[i:i + 2]
            res = time + point
            dump.append(res)
        if down == chunk:
            time = TimeList[i:i + 2]
            point = PointList[i:i + 2]
            res = time + point
            dump.append(res)
    if (dump == []) and (1 in PointList):
        dump = [[TimeList[0], TimeList[-1], 1, 1]]
    else:
        dump = [[TimeList[0], TimeList[-1], 0, 0]]
    return dump


def compare(TrueList, DataList, BORDER=1):
    """
    сравнение двух сигалов, значения беруться из дампов
    [[t0, t1, 0, 1], [t1, t0, 1, 0], ...]
    BORDER - граница по времени сработки, сравниваеться по модулю
    BORDER выбираеться как граница времени сработки деленная на 2
    """
    print('Сравниваю...')
    if len(TrueList) != len(DataList):
        print('Кол-во экстренумов не совпадает, результат может быть неверный...')
    for x, y in zip(TrueList, DataList):
        if (x[2] == 0 and x[3] == 1) and (y[2] == 0 and y[3] == 1):
            delta = x[1] - y[1]
            if abs(delta) <= BORDER:
                print('в пределе +')
            else:
                print(__out(delta, BORDER), 'выпал -')
        elif (x[2] == 1 and x[3] == 0) and (y[2] == 1 and y[3] == 0):
            delta = x[0] - y[0]
            if abs(delta) <= BORDER:
                print('в пределе +')
            else:
                print(__out(delta, BORDER), 'выпал -')
        elif (len(DataList) == 1) and (x[2] == 1 and x[3] == 1) and (y[2] == 1 and y[3] == 1):
            print('Оба в еденице +')
        elif (len(DataList) == 1) and (x[2] == 0 and x[3] == 0) and (y[2] == 0 and y[3] == 0):
            print('Оба в нуле +')
        elif y[2] == 1 and y[3] == 1:
            print('FAIL Постоянно в еденице -')
        elif y[2] == 0 and y[3] == 0:
            print('FAIL Постоянно в нуле -')
        else:
            print('Не та последовательность экстренумов')


def __out(x, y):
    """
    Вывод
    """
    if x < 0:
        a = str(abs(decimal.Decimal(x)) - decimal.Decimal(y))
        return 'Сработал позже предела на ' + a
    elif x > 0:
        a = str(abs(decimal.Decimal(x)) - decimal.Decimal(y))
        return 'Сработал раньше предела на ' + a
