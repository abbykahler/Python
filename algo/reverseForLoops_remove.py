
# Given a string containing space separated words
# Reverse each word in the string.
# If you need to, use .split to start, then try to do it without.

# Input: "hello"
# Output: "olleh"

# Input: "hello world"
# Output: "olleh dlrow"

# Input: "abc def ghi"
# Output: "cba fed ihg"


def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

input_str = 'hello world'

if __name__ == "__main__":
    print('Reverse String using for loop =', reverse_for_loop(input_str))
# Given a string,
# return a new string with the duplicates excluded
# Bonus: Keep only the last instance of each character.

# Input: "abcABC"
# Output: "abcABC"

# Input: "helloo"
# Output: "helo"


# def remove(str, n): 
#     index = 0
#     for i in range(0, n):  
#         for j in range(0, i + 1): 
#             if (str[i] == str[j]): 
#                 break
#         if (j == i): 
#             str[index] = str[i] 
#             index += 1
#     return "".join(str[:index]) 

# str= "helloo"
# n = len(str) 
# print(remove(list(str), n)) 