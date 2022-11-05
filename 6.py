def pres_elect():
    with open('file','r', encoding='UTF-8' ) as file:
        a=file.readline().split()
        overal=0
        dict={}
        last_line=[]
        c=1
        b=[]
        
        for i in a:
            if i!='-1':
                overal+=1
                if i not in dict:
                    dict[i]=1
                else: dict[i]+=1
    keys_values=tuple(dict.items())
    for i in keys_values:
        b.append(i[1])
    b.sort()
    b.reverse()
    for i in b:
        keys=dict.keys()
        for j in keys:
            if dict[j]==i:
                if j not in last_line:
                    last_line.append(j)
                    
                
    for i in last_line:
        print(f'{c}. Партия №{i} | {dict[i]} | {(dict[i]/overal*100):.2f}%')
        c+=1
pres_elect()
