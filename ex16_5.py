from ex16_2 import create_list


ls = create_list()

print(ls)
for i in ls:
    odds = {}
    if abs(i % 2) == 1:
        if len(odds) == 0:
            odds[i] = ls.index(i)
            print(len(odds))
        elif len(odds) == 1:
            print(f'2n if {i}')
            odds[i] = ls.index(i)
            
               
    else:
        odds.clear()

for key, value in odds.items():
    print( key)
    print(value)
    



