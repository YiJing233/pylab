import string
 
#注：python2中的string成员letters在python3中改为了ascii_letters
alphas=string.ascii_letters+'_'
nums=string.digits
 
print('合法标识符检查。。。')
print('测试字符串长度至少为2')
while True:
    myInput=input('键入字符串')
    if len(myInput) > 1:
        if myInput[0] not in alphas:
            print('##标识符首位非法##')
        elif True:
            allChar = alphas + nums
            for otherChar in myInput[1:]:
                if otherChar not in allChar:
                    print('##剩余字符串中存在非法标识符##')
                    break
                else:
                    break
        print('检查结束')
 
if __name__=='__main__':
    test()

" " " dfsfds " " "