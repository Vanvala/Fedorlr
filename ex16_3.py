from ex16_2 import create_list

ls = create_list()
print(ls)
avg = sum(ls)/len(ls)
close = 0


for i in ls:
    if abs(avg-i) < abs(avg-close):
        close = i

print(f'The closest element to average {avg} is {close} ')

