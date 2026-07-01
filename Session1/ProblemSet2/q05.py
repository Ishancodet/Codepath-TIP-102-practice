"""
Session 1 - Problem Set 2 - Problem 5: Concatenate

Write a function concatenate() that takes in a list of strings words 
and returns a string concatenated that concatenates all elements in words.

Example Usage:
words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)

Example Output:
"vengeancedarknessbatman"
""
"""
def concatenate(words):
    sum_word = ""
    for word in words:
        sum_word += word
    return sum_word
words = ["vengeance", "darkness", "batman"]
print(concatenate(words))