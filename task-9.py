""" 
Checking Palindromes
You need to check if each word in a list of words is a palindrome.
if it is palindrome, make the word as key and value as True
else, make the word as key and value as False

Sample Input:
  words = ["radar", "apple", "level", "world"]
Sample Output:
  {"radar":True, "apple":False, "level":True, "world":False}
"""
words = ["radar", "apple", "level", "world"]
palindrome_status = {}
for i in range(len(words)):
    if words[i] == words[i][::-1]:
        palindrome_status[words[i]] = True
    else:
        palindrome_status[words[i]] = False
print(palindrome_status)