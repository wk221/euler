"""
Project Euler - Problem 4.

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest_palindrome = 0

# generate products of two 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        product = str(i * j)  # cast to str for char matching

        if product[0] == product[-1]:
            if product[1] == product[-2]:
                if product[2] == product[-3]:
                    # product is a palindrome, check if largest
                    if int(product) > largest_palindrome:
                        largest_palindrome = int(product)

print(largest_palindrome)
