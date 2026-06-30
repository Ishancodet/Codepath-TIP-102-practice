"""
Session 1 - Problem Set 1 - Question 3
Catchphrases

Problem:
Write a function print_catchphrase() that accepts a string character
as a parameter and prints the catchphrase of the given character:

Pooh -> "Oh bother!"
Tigger -> "TTFN: Ta-ta for now!"
Eeyore -> "Thanks for noticing me."
Christopher Robin -> "Silly old bear."

If the given character does not match one of the characters above,
print "Sorry! I don't know <character>'s catchphrase!"

Example Output:
Oh bother!
Sorry! I don't know Piglet's catchphrase!
"""

# TODO: write your solution here
def print_catchphrase(name):
    if name == "Pooh":
        print("Oh bother!")
    elif name == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif name =="Eeyore":
        print("Thanks for noticing me.")
    elif name == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {name}'s catchphrase!")
print_catchphrase("Piglet")

