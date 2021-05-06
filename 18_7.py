
def stringCount(filename,string):
    """ Считает число повторений в строке файла"""
    counts = 0
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                count = line.count(string)
                # print(f'{line} {count}')
                counts += count
            print(f'В файле {filename} {counts} повторений строки {string}')
    except Exception as ex:
        print(ex) 


stringCount("mail.txt", "edu")
# i = 'm03LMFo4005148@nakamura.uits.iupui.edu'.count('edu')
# print(i)
