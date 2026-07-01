"""
Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".


Example Usage

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)
Example Output:

"I have one power. I never give up. - Batman"
"I have one power. I never nap. - Batman
"""

# TODO: write your solution here
def madlib(Verb):
    print(f"I have one power. I never {Verb}")
madlib("Give up")