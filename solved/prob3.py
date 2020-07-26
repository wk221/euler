"""
Project Euler - Problem 3.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    prime = True  # assume True until proven False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # i is a factor of n -> n is not prime
            prime = False
            break

    return prime


largest_prime_factor = 0

for j in range(1, int(sqrt(600851475143) + 1)):
    if 600851475143 % j == 0:  # j is a factor of 600851475143, check if prime
        if is_prime(j):
            if j > largest_prime_factor:  # check if largest_prime_factor
                largest_prime_factor = j

print(largest_prime_factor)
