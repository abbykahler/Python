
# Given a list of strings
# return a sum to represent how many times each list item is found (a frequency table)

# Input: ["a", "a", "a"]
# Output: {
#   "a": 3,
# }

# Input: ["a", "b", "a", "c", "B", "c", "c", "d"]
# Output: {
#   "a": 2,
#   "b": 1,
#   "c": 3,
#   "B": 1,
#   "d": 1,
# } 




def freq(someList):
    freqTable = {}
    for i in range(len(someList)):
        if someList[i] in freqTable:
            freqTable[someList[i]] += 1
        else:
            freqTable[someList[i]] = 1
    
    return freqTable

Alist = ["a", "b", "a", "c", "B", "c", "c", "d"]

print(freq(Alist))





# Reverse Word Order
# Given a string of words (with spaces)
# return a new string with words in reverse sequence.

# Input: "This is a test"
# Output: "test a is This"



input="This is a test"
somestring=input.split(" ")
temp=[]
i=-1
for j in range(len(somestring)):
    temp.append(somestring[i])
    i-=1

newString1 = ''
for a in range(len(temp)):
    newString1 += temp[a] + ' '

# print(temp)
print(newString1)