import random

new_list = [random.randint(1, 200) for i in range(10)]

#for i in range(10):
#   num = random.randint(1, 200)
#   new_list.append(num)

print(new_list)

def dif_max_min(L):
    """ calculate differance beetwin max and min number in list """
    min_num = min(L)
    max_num = max(L)

    return max_num - min_num

print(dif_max_min(new_list))




