"""
Project Euler - Problem 6.

(https://projecteuler.net/problem=6)
"""

# calculate the sum of the squares
sum_of_squares = 0

for i in range(1, 101):
    sum_of_squares += i**2

# calculate the square of the sum
sum = 0
square_of_sum = 0

for j in range(1, 101):
    sum += j

square_of_sum = sum**2

print(square_of_sum - sum_of_squares)
