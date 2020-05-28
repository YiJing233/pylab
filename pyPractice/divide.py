
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (high + low) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else :
            low = mid + 1
    return None



my_list = [1,3,4,5,7,32,343,878,1322]

print(my_list)
# print(binary_search(my_list.sort,3))

a = len(list)
print(a)