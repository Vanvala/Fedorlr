

def create_list():
    ''' create  random list from -1000 to 1000 with 1000 elements'''

    import random
    new_list = [random.randint(-1000,1000) for i in range(1000)]
    return new_list

x = create_list()
print(x)

max_num = max(x)
min_num = min(x)
min_index = x.index(min_num)
max_index = x.index(max_num)

if max_index > min_index:
    new_list = x[min_index+1:max_index]
else:
    new_list = x[max_index+1:min_index]

negative_list = [i for i in new_list if i < 0]

print(f'Number of negative element in list between max and min number {len(negative_list)}')