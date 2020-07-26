"""
Project Euler - Problem 7.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


primes = []  # list to store generated primes
i = 2  # start with the first prime number

# generate 10001 primes using is_prime(n)
while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
    i += 1

print(primes[-1])
