#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    sum = 0
    weights_sum = 0
    for element in my_list:
        sum += element[0] * element[1]
        weights_sum += element[1]
    return sum / weights_sum
