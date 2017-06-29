# -*- coding: utf-8 -*-

"""
author: decard
22.05.17
"""

import digit

time_1 = [0.120, 0.121, 0.122, 0.123, 0.124, 0.125, 0.126, 0.127, 0.128, 0.129]
time_2 = [0.220, 0.221, 0.222, 0.223, 0.224, 0.225, 0.226, 0.227, 0.228, 0.229]

gpio_0 = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]

a1 = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
a2 = [0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
a3 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
a4 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
a5 = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
a6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
a7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a8 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
a9 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
a0 = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0]

time_1 = digit.rolltime(gpio_0, time_1)
time_2 = digit.rolltime(gpio_0, time_2)

dump_a = digit.searchpoint(a1, time_1)
dump_b = digit.searchpoint(a9, time_2)

digit.compare(dump_a, dump_b, BORDER=0.001)
