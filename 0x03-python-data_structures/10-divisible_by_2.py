#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    div_2 = []
    for num in my_list:
        if num % 2 == 0:
            div_2.append(True)
        else:
            div_2.append(False)
    return div_2
