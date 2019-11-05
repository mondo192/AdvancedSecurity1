#!/usr/bin/python3
from random import randint


def miller_rabin_test(n):
    q = n - 1
    k = 1

    # find integers k, q with k > 0, q being odd so that (n - 1) = 2 ^ k * q
    while q % 2 == 0:
        q = (n - 1) // pow(2, k)
        k += 1

    # select a random integer a, 1 < a < n - 1
    a = randint(1, n - 1)

    # if a ^ q mod n = 1 then return inconclusive
    if pow(a, q, n) == 1:
        return 'Inconclusive, probably not a prime number.'

    # if a ^ (2 ^ i) * q mod n = n - 1 then return inconclusive
    for i in range(1, k):
        if pow(a, (pow(2, i) * q), n) == n - 1:
            return 'Inconclusive, probably not a prime number.'

    # return conclusive
    return 'Composite, definitely not a prime number.'


if __name__ == '__main__':
    print(f'The result for 101: {miller_rabin_test(101)}')
    print(f'The result for 592701729979: {miller_rabin_test(592701729979)}')
