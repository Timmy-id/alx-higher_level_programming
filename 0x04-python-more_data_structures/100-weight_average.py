#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wgts = 0
    avg = 0
    for i in my_list:
        wgts += i[-1]
        avg += i[0] * i[1]
    return avg / wgts
