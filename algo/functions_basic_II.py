# 1 Countdown
# num = 5
# def countdown(num):
#     new_list = []
#     for x in range(num,-1,-1):
#         new_list.append(x)
#     return new_list
# print(countdown(5))


# 2 Print and Return  
# list=[1,2]
# def print_return(list):
#     print (list[0])
#     return list[1]
# print (print_return(1,2))




# 3 First Plus Length
# def first_plus_length(list):
#     sum = list[0] + len(list)
#     return sum



# 4 Values Greater than Seconds
def value_greater(list):
    new_list = []
    for i in list:
        if i > list[1]:
            new_list.append(i)
    print(len(new_list))
    if len(new_list) < 2:
        return False
    else:
        return new_list 
    



# 5 This Length, That Value
def length_value(size,value):
    list = [value] * size
    return list
    
    
    