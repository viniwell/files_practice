
def glas_soglas():
    soglas_count=0
    glas_count=0
    soglas='б,в,г,д,ж,з,й,к,л,м,н,п,р,с,т,ф,х,ц,ч,ш,щ'.split(',')
    glas='а,е,ё,и,о,у,ы,э,ю,я'.split(',')
    with open('file', 'r', encoding='UTF-8') as file:
        for i in list(file.readlines()):
            print(i, end='')
            a=map(str, i.split())
            for i in a:
                x=i.lower()
                if x[0].lower() in soglas:
                    soglas_count+=1
                elif x[0].lower() in glas:
                    glas_count+=1
    print('')
    if soglas_count>glas_count:
        print('Согласных')
    elif glas_count>soglas_count:
        print('Гласных')
    else: print('Одинаково')
glas_soglas()