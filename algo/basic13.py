
# Print 1 - 255:

def print255():
    for i in range(1, 256):
        print(i)

print255()

# Print Odds 1 - 255:

def printOdd255():
    for i in range(1, 256, 2):
        print(i)

printOdd255()

# Print Ints and Sum 1 - 255:

def prIntSum():
    sum = 0
    for i in range(256):
        print("Current value: ", i)
        sum += i
        print("sum: ", sum)

prIntSum()

listy_list = [1, 2, 3, 4, 5]

# Iterate and Print List:

def iteratePrint(takenList):
    for i in takenList:
        print(i)

iteratePrint(listy_list)

# Find and Print Max:

def maximum(takenList):
    max = takenList[0] 
    for num in takenList:      
        if num > max:
            max = num  

print(maximum(listy_list))

# Get and Print Average:

def average(num):
    sum = 0
    for i in num:
        sum = sum + i           

    avg = sum / len(num)
    return avg

# List with Odds:

def oddList():
    retList = []

    for i in range(1, 256, 2):
        retList.append(i)
    
    return retList

print(oddList())

# Square the values:

def squareVal(givenList):
    for i in range(len(givenList)):
        givenList[i] = givenList[i] * givenList[i]

    return givenList

print(squareVal(listy_list))

# Greater than Y

def greaterThanY(takenList, y):
    count = 0

    for i in range(len(takenList)):
        if takenList[i] > y:
            count += 1

    return count

anotherList = [1, 2, 3, 4, 6, 67]

print(greaterThanY(anotherList, 2))

# Zero out Negatives:

def zeroNeg(takenList):
    for i in range(len(takenList)):
        if takenList[i] < 0:
            takenList[i] = 0

    return takenList


yetAnotherList = [-3, 4, 23, -234, 4, 2, -4, 0]

print(zeroNeg(yetAnotherList))

# Max Min Average:

def maxMinAvg(takenList):
    sumTotal = 0
    average = 0
    minimum = takenList[0]
    maximum = takenList[-1]
    
    for item in takenList:
        sumTotal = item + sumTotal
        if item < minimum: 
            minimum = item
        if item > maximum: 
            maximum = item
    average = sumTotal / len(takenList)

    print(f"Max: {maximum}, Minimum: {minimum}, Average: {average}")

maxMinAvg(anotherList)

# Shift Array Values:

def shiftValues(takenList):
    temp = takenList[0]

    for i in range(len(takenList) - 1):
        takenList[i] = takenList[i + 1]
        takenList[i + 1] = temp
    
    takenList[len(takenList) - 1] = 0

    return takenList

lastList = [1, 2, 3, 4, 5]

print(shiftValues(lastList))

# Swap String for Array Negative Values:

def swapString(takenList):
    for item in range(len(takenList)): 
        if takenList[item] < 0:
            takenList[item] = "Dojo"

    return takenList

realLastList = [-34, 54, -2, 5, 2]

print(swapString(realLastList))