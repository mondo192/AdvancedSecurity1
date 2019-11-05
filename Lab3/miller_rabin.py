from random import randint


def miller_rabin_test(n):
    q = n - 1
    k = 1

    print(f'Testing: {n}')

    # find integers k, q with k > 0, q being odd so that (n - 1) = 2 ^ k * q
    while q % 2 == 0:
        q = (n - 1) // pow(2, k)
        k += 1

    # select a random integer a, 1 < a < n - 1
    a = randint(1, n - 1)

    # if a ^ q mod n = 1 then return inconclusive
    if pow(a, q, n) == 1:
        return "Inconclusive"

    # if a ^ (2 ^ i) * q mod n = n - 1 then return inconclusive
    for i in range(k - 1):
        if pow(a, (pow(2, i) * q), n) == n - 1:
            return "Inconclusive"

    # return conclusive
    return "Composite"


if __name__ == '__main__':
    print(miller_rabin_test(101))
    print(miller_rabin_test(592701729979))
    # print(f'Result: {miller_rabin_test(101)}')
    # print(f'Result: {miller_rabin_test(592701729979)}')




