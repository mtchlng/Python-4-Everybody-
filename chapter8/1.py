
def middle(y):
    newList = y[1:]
    del newList[-1]
    return newList

my_list = [1, 2, 3, 4]

middleList = middle(my_list)
print(middleList)
