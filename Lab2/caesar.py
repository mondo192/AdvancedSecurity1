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
        print("Incorrect usage. Usage: python caesar <key>")
        return False

    # assign keyword to 'key' variable and validate format (numeric chars only)
    if not sys.argv[1].isdigit():
        print("Invalid key. Use only numeric characters.")
        return False
    else: # convert cmd line arguemnet to an integer value for shift key
        return int(sys.argv[1])


def encrypt(plaintext, key):
    ciphertext = ''
    for c in plaintext:
        # not in alphabet or is a space character therefore dont encrypt
        if not c.isalpha() or c.isspace():
            # append to buffer variable
            ciphertext += c
        else: # is in alphabet therfore do encryption on character by character basis
            if c.isupper():
                # find constrained ascii value for given character with the shift key added
                c_ascii = ((ord(c) - ord('A')) + key) % 26 + ord('A')
                # converted ascii value to a character and append to buffer
                ciphertext += chr(c_ascii)
            else: # letter if lowercase
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
                # find constrained ascii value for given character with the shift key subtracted
                p_ascii = ((ord(p) - ord('A')) - key) % 26 + ord('A')
                # converted ascii value to a character and append to buffer
                plaintext += chr(p_ascii)
            else:
                p_ascii = ((ord(p) - ord('a')) - key) % 26 + ord('a')
                plaintext += chr(p_ascii)
    return plaintext


if __name__ == "__main__":
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
