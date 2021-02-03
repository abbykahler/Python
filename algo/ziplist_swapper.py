
# Zip lists into dictionary

# Given two lists, create a dictionary containing keys from the first list, 
# and values from the second.

# Input: ["abc", 3, "yo"], [42, "wassup", True]
# Output: {
#   "abc": 42,
#   3: "wassup",
#   "yo": True,
# }

# option1
# list1 = ["abc", 3, "yo"]
# list2 = [42, "wassup", True]
# new_dict ={}
# def zip_list(list1, list2):
#     for i in range(0,len(list1)):
#         new_dict[list1[i]] = list2[i]
#     return new_dict

# print (zip_list(list1, list2))

# option2
# list1 = ["abc", 3, "yo"]
# list2 = [42, "wassup", True]

# def zip_list(list1, list2):
#     newdict = {list1[i]: list2[i] for i in range(len(list1))}
#     return newdict

# print (zip_list(list1, list2))



# Invert Hash

# Given a dictionary, return a new dictionary that has the keys and the values 
# swapped so that the keys become the values and the values become the keys

# Input: { "name": "Zaphod", "charm": "high", "morals": "dicey" }
# Output: { "Zaphod": "name", "high": "charm", "dicey": "morals" }



# old_dict= {"name": "Zaphod", "charm": "high", "morals": "dicey"}
# new_dict = {} 
# for key, value in old_dict.items(): 
#     if value in new_dict: 
#         new_dict[value].append(key) 
#     else: 
#         new_dict[value]=[key] 

# for i in new_dict: 
#     print(i, ":",new_dict[i])

def swapper(incoming):
    new_dict = {}
    for key, val in incoming.items():
        new_dict[val] = key
    return new_dict


print(swapper({"name": "Zaphod", "charm": "high", "morals": "dicey"}))
