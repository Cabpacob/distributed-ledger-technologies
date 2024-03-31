import math
import random

MIN_PRIME = 2 ** 63
MAX_PRIME = 2 ** 64


def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def is_prime(n):
    return miller_rabin_test(n, 50)


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
