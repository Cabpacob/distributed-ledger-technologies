import math
import random

MIN_PRIME = 2 ** 31
MAX_PRIME = 2 ** 32


def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def generate_prime_number():
    while True:
        num = random.randint(MIN_PRIME, MAX_PRIME)
        if is_prime(num):
            return num


def generate_coprime_number(number):
    while True:
        result = random.randint(2, number)
        if math.gcd(result, number) == 1:
            return result


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y
