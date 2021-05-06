from ex16_2 import create_list


ls = create_list()

new_ls = []

for i in ls:
    if i % 2 == 0 or i % 5 == 0:
        new_ls.append(i)
 
print(f' The length of {new_ls} is {len(new_ls)}')