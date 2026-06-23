"""
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.


Example Usage

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
Example Output:

[1, 2, 3, 6]
[1]
"""

# TODO: write your solution here
def split_haycorns(n):
    divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor 
print(split_haycorns(6))
    



