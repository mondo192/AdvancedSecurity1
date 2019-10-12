#!/usr/bin/python3

import sys


def write_data_to_disk(data):
    workfile = input('\nSave file as: ')
    with open(workfile, 'w') as f:
        f.write(data)
        f.close()


def read_data_from_disk():
    workfile = input('\nEnter the path to the file for reading: ')
    with open(workfile) as f:
        plaintext = f.read()
        f.close()
    return plaintext


def validate_key():
    # confirm exactly two arguments entered on command line (program name and keyword)
    if len(sys.argv) != 2:
        print("Incorrect usage. Usage: python vigenere <key>")
        return False

    # assign keyword to 'key' variable and validate format (alpha chars only)
    if not sys.argv[1].isalpha():
        print("Invalid key. Use only alphabetical characters.")
        return False
    else:
        return sys.argv[1]


def encrypt(plaintext, key):
    output = ''
    key_len = len(key)
    letter_counter = 0

    # loop through plaintext, char by char, encrypting using keyword provided by user
    for c in plaintext:
        # isalpha() include whitespace, second condition prints whitespace without encryption
        if not c.isalpha() or c.isspace():
            output += c
        else:
            # encrypt uppercase letter of plaintext
            # if current keyword char is lowercase, refer to uppercase counterpart
            if c.isupper():
                # refer to current char in keyword, by cycling through using mod and length of keyword
                cipher_char = key[letter_counter % key_len].upper()
                cipher_char_ascii = ord(cipher_char.upper()) if cipher_char.islower() else ord(cipher_char)
                output += chr(((ord(c) - ord('A')) + (cipher_char_ascii - ord('A'))) % 26 + ord('A'))
            # encrypt lowercase letters in plaintext
            # refer to lowercase counterpart if current keyword char is uppercase
            else:
                cipher_char = key[letter_counter % key_len]
                cipher_char_ascii = ord(cipher_char.lower()) if cipher_char.isupper() else ord(cipher_char)
                output += chr(((ord(c) - ord('a')) + (cipher_char_ascii - ord('a'))) % 26 + ord('a'))
            # advance position in keyword to next char
            letter_counter += 1
    return output


def decrypt(ciphertext, key):
    output = ''
    key_len = len(key)
    letter_counter = 0

    # loop through plaintext, char by char, encrypting using keyword provided by user
    for p in ciphertext:
        # isalpha() include whitespace, second condition prints whitespace without encryption
        if not p.isalpha() or p.isspace():
            output += p
        else:
            # encrypt uppercase letter of plaintext
            # if current keyword char is lowercase, refer to uppercase counterpart
            if p.isupper():
                # refer to current char in keyword, by cycling through using mod and length of keyword
                plain_char = key[letter_counter % key_len].upper()
                plain_char_ascii = ord(plain_char.upper()) if plain_char.islower() else ord(plain_char)
                output += chr(((ord(p) - ord('A')) - (plain_char_ascii - ord('A'))) % 26 + ord('A'))
            # encrypt lowercase letters in plaintext
            # refer to lowercase counterpart if current keyword char is uppercase
            else:
                plain_char = key[letter_counter % key_len]
                plain_char_ascii = ord(plain_char.lower()) if plain_char.isupper() else ord(plain_char)
                output += chr(((ord(p) - ord('a')) - (plain_char_ascii - ord('a'))) % 26 + ord('a'))
            # advance position in keyword to next char
            letter_counter += 1
    return output


if __name__ == '__main__':
    key = validate_key()
    if not key:
        sys.exit(0)

    running = True
    while running:
        menu = int(input(
            '\n1. Encrypt file\n'
            '2. Decrypt file\n'
            '3. Exit\n\n'
            'Enter your choice: '
        ))
        if menu == 1:
            plaintext = read_data_from_disk()
            encrypted = encrypt(plaintext, key)
            print('\nEncrypting...\n"' + plaintext + '"\n\nKey: ' + str(key) + '\n\nCiphertext...\n' + encrypted)
            write_data_to_disk(encrypted)
        elif menu == 2:
            ciphertext = read_data_from_disk()
            decrypted = decrypt(ciphertext, key)
            print('\nDecrypting...\n"' + ciphertext + '"\n\nKey: ' + str(key) + '\n\nPlaintext...\n' + decrypted)
            write_data_to_disk(decrypted)
        elif menu == 3:
            print('Exiting...')
            running = False
        else:
            print('Invalid selection. Try again')