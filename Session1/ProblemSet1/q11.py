"""
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r removed from it.


Example Usage

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
Example Output:

"suspcous"
""
"Hunny"
"""

# TODO: write your solution here
def tiggerfy(s):
    result = ""                              # empty string to build onto
    for letter in s:
        if letter.lower() not in "tiger":     # is this letter NOT one of the banned ones?
            result += letter                   # keep it
    return result
print(tiggerfy("sonic"))
