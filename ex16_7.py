from ex16_2 import create_list

ls = create_list()
avg = sum(ls)/len(ls)
avg_list = []

for i in ls:
    if i > avg:
        avg_list.append(i)

print(f'Number of elements more then average {avg} is {len(avg_list)}')
