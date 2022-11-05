def empty_booked_place():    
    with open('file','r',encoding='UTF-8') as file:
        empty_place=0
        a=file.readlines()
        for i in a:
            for j in i:
                if j=='0':
                    empty_place+=1
    print(empty_place)
    with open('file','r',encoding='UTF-8') as file:
        row_column=input().split()
        row=int(row_column[0])
        column=int(row_column[1])
        for i in range(row-1):
            file.readline()
        a=file.readline().split()
        if a[column-1]=='0':
            print('This place is empty.')
        else:
            print('This place is booked.')
empty_booked_place()