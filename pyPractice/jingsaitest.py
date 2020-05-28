a = input()

mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

for i in range (1,10000):
    for month in mon:
        if str(i)+month in a:
            print(str(i) + month)
        else:
            print('2000Jan')