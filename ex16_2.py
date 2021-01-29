

def create_list():
    ''' create  random list from -1000 to 1000 with 1000 elements'''

    import random
    new_list = [random.randint(-1000,1000) for i in range(1000)]
    return new_list
