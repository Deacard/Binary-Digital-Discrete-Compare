# -*- coding: utf-8 -*-
"""
modul digit
author: decard
22.05.17
"""


def rolltime(UpPointList, TimeList):
    """
    TimeList - список временных отметок]
    UpPointList - список относительно которого будем сдвигать время,
    сдвигаем от первого вхождения '1'
    """
    if UpPointList[0] == 0:
        item = UpPointList.index(1)
    elif UpPointList[0] == 1:
        return(TimeList)
    NewTime = []
    for i in TimeList:
        PointTime = i - TimeList[item]
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
    return dump


def compare(TrueList, DataList, BORDER=1):
    """
    сравнение двух сигалов, значения беруться из дампов
    BORDER - граница по времени сработки, сравниваеться по модулю
    """
    print('Сравниваю...')
    for x, y in zip(TrueList, DataList):
        if x[3] and y[3] == 1:
            delta = x[1] - y[1]
            if abs(delta) < BORDER:
                print(delta, 'good')
            else:
                print(delta, 'bed')
        elif x[2] and y[2] == 1:
            delta = x[0] - y[0]
            if abs(delta) < BORDER:
                print(delta, 'good')
            else:
                print(delta, 'bed')
        else:
            print('Не та последовательность экстренумов')


def _out(a, delta):
    """
    Более полный вывод
    """
    if abs(a) <= delta:
        print(a, '+ в пределе')
    else:
        print(a, '- выпал')
    if a < 0:
        print('сработал позже')
    elif a > 0:
        print('сработал раньше')
    elif a == 0:
        print('попал')
