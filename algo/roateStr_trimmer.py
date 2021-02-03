
# String: Rotate String
# Create a standalone function that accepts a string and an 
# integer, and rotates the characters in the string to the 
# right by that given integer amount.

# Input: "Hello World", 0
# Output: "Hello World"

# Input: "Hello World", 1
# Output: "dHello Worl"

# rotateStr="Hello World", 2
# Output: "ldHello Wor"

# Input: "Hello World", 4
# Output: "orldHello W"


# def rotateStr(str, num):
#     new_str= ""
#     for i in range(len(str)-num, len(str)):
#         new_str += str[i]
#     for j in range(len(str)-num):
#         new_str += str[j]
#     print(new_str)
# rotateStr("Hello World", 4)







# String: Trim
# Given a string that may have extra spaces at the start and the end,
# return a new string that has the extra spaces at the start and the end trimmed (removed)
# do not remove any other spaces.


# Input: "   hello world     "
# Output: "hello world"


# def trimmmer(str):  
#     space = False
#     for i in range(len(str)): 
#         if str[i] =="":   
            
            
            
def trimmer(str):
    new_words = str.split()
    new_str = ""
    print (new_words)
    for i in range(len(new_words)):
        if i == len(new_words):
            new_str += new_words[i]

        else:
            new_str += new_words[i] + ' '
            

    return new_str

print(trimmer("   hello     world    "))

