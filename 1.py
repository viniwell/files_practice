def printing():
    a=[str(x) for x in input().split()]
    with open("file",'w',encoding='UTF-8') as file:
        for i in a:
            file.write(str(i)+'\n')
    return file
printing()
