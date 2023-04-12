my_list = [1,2,3,4]

def myfunc(num):
    return num + 1

lemon = list(map(myfunc, my_list))
print(lemon)
print(my_list)