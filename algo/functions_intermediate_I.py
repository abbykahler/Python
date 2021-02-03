# 1 Biggie Size
# mylist = [ 1, 2, 3, -7]
# print(mylist)
# for i in range(len(mylist)):
#     if mylist[i] < 0
#     mylist[i]= "big"
    
# print(mylist)



# 2 count postives
# list1 = [10, -21, -4, -45, -66, 93, 11] 
# count = 0
# num = 0     
# while(num < len(list1)): 
#     if list1[num] >= 0: 
#          count += 1
# print(count)
# list()


# # 3 sum total
# def sum_total(listist):
#     sum = 0
#     for i in listist:
#         sum = sum + i
#     return sum

# print(sum_total([1,2,3,4]))



# #  4 Average
def average(num):
    sum = 0
    for i in num:
        sum = sum + i           

    avg = sum / len(num)
    return avg

print(average([1,2,3,4]))


# 5 Length

# def length(list):
#     count=0
#     for i in list:
#         count=count+1
#     return count

# list1=[37,2,1,-9]
# print(count())


# 6 Minimum
# def minimum(list):
#     min = list[0] 
#     for num in list:      
#         if num < min:
#             min = num  
    # if list[i] < 0:
    # return false
#     return min

# print min([1,2,3,-1])



# 7 Maximum

# def maximum(list):
#     mx = list[0] 
#     for num in list:      
#         if num > max:
#             max = num  
#     if list[i] < 0:
    # return false
#     return min

# print min([1,2,3,-1])




# def maxMinAvg(list):
#     sumTotal = 0
#     average = 0
#     minimum = list[0]
#     maximum = list[-1]
#     list_length = len(list)
#     for item in list:
#         sumTotal = item + sumTotal
#         if item < minimum: 
#             minimum = item
#         if item > maximum: 
#             maximum = item
#     average = sumTotal / list_length






# 8 Ultimate Analysis
# 9 Reverse List





def swapString(takenList):
    for item in range(len(takenList)): 
        if item < 0:
            item = "Dojo"

    return takenList











