# Task1
"""
Task: Format and Analyze a Sentence
Description: Given a sentence, perform the following operations:

- Convert the entire sentence to uppercase.
- Count the number of occurrences of the letter 'E'.
- Replace all occurrences of the word "bad" with "good".
- Capitalize the first letter of each word.
- Find the length of the modified sentence.
- Extract a substring from the modified sentence, Get the first 10 characters.

Sample Input:
-------------
sentence = "This is a bad example of a bad situation."

Sample Output:
--------------
Uppercase: THIS IS A BAD EXAMPLE OF A BAD SITUATION.
Occurrences of 'E': 2
Replaced: This is a good example of a good situation.
Capitalized: This Is A Good Example Of A Good Situation.
Length: 43
Sliced Substring: This is a 
"""

sentence = "This is a bad example of a bad situation."
sentence1 = sentence.upper()
print(f"Uppercase: {sentence1}")
print(f"Occurences of 'E': {sentence1.count('E')}")

sentence = sentence.replace("bad", "good")
print(f"Replaced: {sentence}")
print(f"Length: {len(sentence)}")
print(f"Sliced Substring: {sentence[:10]}")