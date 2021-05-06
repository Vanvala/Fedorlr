
def myGrep(filename,string):
    """ Возвращает в строке файла"""
    counts = 0
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                if string in line:
                    print(line)
           
    except Exception as ex:
        print(ex) 


myGrep("mail.txt", "edu")
