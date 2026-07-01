"""
Session 1 - Problem Set 2 - Problem 6: Squared

Write a function squared() that accepts a list of integers numbers 
as a parameter and squares each item in the list. Return the squared list.

Example Usage:
numbers = [1, 2, 3]
squared(numbers)

Example Output:
[1, 4, 9]
"""

# TODO: write your solution here
def squared(numbers):
    double_numbers = []
    for number in numbers:
        double_numbers.append(number*2)
    return double_numbers
numbers = [1, 2, 3]
print(squared(numbers))

    