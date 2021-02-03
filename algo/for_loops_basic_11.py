# 1 Biggie size
# def biggie_size(list):
#     return_list = []
#     for item in list:
#         if item > 0:
#             return_list.append ("big")
#         else:
#             return_list.append (item)
#     return return_list
# print(biggie_size([-1,3,5,-5]))


# 2 Count Positives
# def count_postives(list):
#     count = 0
#     for item in list:
#         if item > 0:
#             count = count + 1
#     list[len(list)] = count
#     return list 
    
    
# 3 Sum Total
# def sum_total(list):
#     sum = 0
#     for item in list:
#         sum = item + sum
#     return sum


# 4 Average
# def average(list):
#     sum = 0
#     for item in list:
#         sum = item + sum
#     return sum / len(list)



# 5 length
# def length(list): 
#     count = 0
#     for item in list:
#         count = count +1
#     return count



# 6 Minimum
# def minimum(list):
#   if len(list) = 0:
#     return False
#     min = list[0]
#     for item in list:
#         if item < min: 
#             min = item
#     return min


# 7 maximum 
# def maximum(list):
# if len(list) = 0:
#     return False
#     max = list[0]
#     for item in list:
#         if item > max: 
#             max = item
#     return max

# 8 ultimate analysis 
# def ultimate_analysis(list):
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
#     return {'sumTotal': sumTotal, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': list_length }


# 9 reverse list
# def reverse_list(list):
#     length_list = len(list)
#     new_list = []
#     for i in range(length_list-1,-1,-1):
#         new_list.append(list[i])
#     return new_list
# print(reverse_list([37,2,1,-9]))