def calc_max():
    with open('file', 'r', encoding='UTF-8') as file:
        a=[int(x) 
        for x in list(file.readlines()) 
        if x[:-1].isnumeric()]
    with open('file', 'a', encoding='UTF-8') as file:
        file.write(str(sum(a))+'\n')
        file.write(str(max(a))+'\n')
calc_max()