"""
Project Euler - Problem 10.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


j = 2  # first prime
primes_sum = 0

while j < 2000000:
    if is_prime(j):
        primes_sum += j
    j += 1

print(primes_sum)
