def triangles():#函数用来输出杨辉三角的每一行，以列表的形式呈现
    L = [1]
    while True:
        yield L
        L = L + [0]
        L = [L[i-1]+L[i] for i in range(len(L))]
        #print(L)#检查了下yield L 暂停时L的内容


'''
之前的语句中，yield L 之后是 L.append(0)
这样做的问题是，append是本地操作，是在原先的内存块上进行的，在接下来的操作里，没有被覆盖掉

同理，用L += [0] 也是在本地操作，结果会是一样的

如果想将结果改变，需要将语句改为 L = L + [0] 属于重新赋值，将一个新的对象给L引用


'''

n = 0
results = []
for t in triangles():
    results.append(t)
    print(t)
    n = n + 1
    if n == 10:
        break

for o in results:
    print(o)
#发现results列表内的元素比L中的多了一个零？
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')