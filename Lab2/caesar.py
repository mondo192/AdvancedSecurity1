#!/usr/bin/python3

import sys


def validate_key():
    # confirm exactly two arguments entered on command line (program name and keyword)
    if len(sys.argv) != 2:
        print("Incorrect usage. Usage: python caesar <key>")
        return False

    # assign keyword to 'key' variable and validate format (alpha chars only)
    if not sys.argv[1].isdigit():
        print("Invalid key. Use only numeric characters.")
        return False
    else:
        return int(sys.argv[1])


def encrypt(plaintext, key):
    ciphertext = ''
    for c in plaintext:
        if not c.isalpha() or c.isspace():
            ciphertext += c
        else:
            if c.isupper():
                c_ascii = ((ord(c) - ord('A')) + key) % 26 + ord('A')
                ciphertext += chr(c_ascii)
            else:
                c_ascii = ((ord(c) - ord('a')) + key) % 26 + ord('a')
                ciphertext += chr(c_ascii)
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''
    for p in ciphertext:
        if not p.isalpha() or p.isspace():
            plaintext += p
        else:
            if p.isupper():
                p_ascii = ((ord(p) - ord('A')) - key) % 26 + ord('A')
                plaintext += chr(p_ascii)
            else:
                p_ascii = ((ord(p) - ord('a')) - key) % 26 + ord('a')
                plaintext += chr(p_ascii)
    return plaintext


if __name__ == "__main__":
    key = validate_key()
    if not key:
        sys.exit(0)

    plaintext = input("Enter text to be encrypted: ")
    encrypted = encrypt(plaintext, key)
    print('Encrypting "' + plaintext + '" with a key of "' + str(key) + '," using Caesar’s cipher, yields the ciphertext "' + encrypted + '."')

    ciphertext = input("Enter text to be decrypted: ")
    decrypted = decrypt(ciphertext, key)
    print('Decrypting "' + ciphertext + '" with a key of "' + str(key) + '," using Caesar’s cipher, yields the plaintext "' + decrypted + '."')