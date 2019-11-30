from random import randint


def extended_eucild(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_eucild(b % a, a)
        return g, y - (b // a) * x, x


def modular_inverse(a, b):
    g, x, _ = extended_eucild(a, b)
    if g == 1:
        return x % b


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def get_coprime_of_phi(phi):
    while True:
        e = randint(2, phi)
        if gcd(e, phi) == 1:
            return e


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_coprime_of_phi(phi)
    d = modular_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(public, message):
    cipher = [pow(ord(c), public[0], public[1]) for c in message]
    return cipher


def decrypt(private, message):
    plain = [chr(pow(c, private[0], private[1])) for c in message]
    return plain


def miller_rabin_test(n, k=128):
    # Prime Test, returns True when prime
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def prompt():
    while True:
        try:
            number = int(input('Enter a number (must be prime): '))
            if miller_rabin_test(number):
                return number
            else:
                print('Not prime. Try again')
        except ValueError:
            print('Oops! That was no valid number. Try again...')
            continue


if __name__ == '__main__':
    num1 = prompt()
    num2 = prompt()

    pub_key, priv_key = generate_keypair(num1, num2)
    print(f'Public key: {pub_key}, Private key: {priv_key}')

    data = input('Enter a message (to encrypt): ')

    encrypted_message = encrypt(pub_key, data)
    decrypted_message = decrypt(priv_key, encrypted_message)

    print('Encryted message is:', ''.join(str(e) for e in encrypted_message))
    print('Decryped message is:', ''.join(str(d) for d in decrypted_message))
