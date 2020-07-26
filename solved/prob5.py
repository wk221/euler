"""
Project Euler - Problem 5.

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""


def evenly_divisible_up_to(n, final_divisor):
    """Return True if n is evenly divisible by 1:final_divisor."""
    divisible = True  # assume True until proven False

    for i in range(1, final_divisor + 1):
        if n % i != 0:  # remainder -> not evenly divisible
            divisible = False
            break

    return divisible


j = 2520
while not evenly_divisible_up_to(j, 20):
    j += 2520

print(j)
