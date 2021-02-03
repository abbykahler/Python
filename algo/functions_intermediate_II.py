# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # 1
# x[1][0] = 15
# print(x[1][0])

# # 2
# students[0]['last_name'] = 'Bryant'
# print(students)

# # 3
# sports_directory ["soccer"][0] = 'Andres'
# print(sports_directory)

# # 4
# z[0]['y'] = 30
# print(z)








# def iterateDictionary(dictionary):
#     for item in dictionary:  
#         print('first_name - ' + str(item['first_name']) + ', last_name - ' + str(item['last_name']))

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(students) 



# def iterateDictionary2(key_name, some_list): 
#         for item in some_list:  
#             print(item[key_name])

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary2('first_name',students) 

def printInfo(some_dict): 
    for key in some_dict: 
        count = len(some_dict[key])
        print(str(count) + ' ' + key.upper())
        for item in some_dict[key]: 
            print(item)
        print('')
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)


