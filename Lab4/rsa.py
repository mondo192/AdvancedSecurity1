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


if __name__ == '__main__':
    num1 = 17
    num2 = 11
    public, private = generate_keypair(num1, num2)
    print(f'Public key: {public}, Private key: {private}')
    message = input('Enter a message: ')
    encrypted_message = encrypt(public, message)
    decrypted_message = decrypt(private, encrypted_message)

    print('Encryted message is:', ''.join(str(e) for e in encrypted_message))
    print('Decryped message id:', ''.join(str(d) for d in decrypted_message))
