import os


class CaesarCipher:
    def __init__(self, m, a):
        try:
            self.message = self.get_data(file_path=m)
            self.alphabet = self.get_data(file_path=a)
        except OSError as e:
            print(e)

    @staticmethod
    def get_data(file_path):
        with open(file_path) as file:
            data = file.read()
            filename = os.path.basename(file_path)
            print(f'{filename} was found!')
        return data

    def brute_force_key(self):
        ciphertext = self.message
        print(f'\n\t\t {ciphertext} KEY')
        for k in range(len(self.alphabet)):
            translated = ''
            for c in ciphertext:
                if c.isalpha():
                    num = self.alphabet.find(c)
                    num = num - k
                    if num < 0:
                        num = num + len(self.alphabet)
                    translated = translated + self.alphabet[num]
                else:
                    translated = translated + c
            print(f'\t{k} \t {translated}', end='')
        k = input('Enter the key that you found: ')
        return k

    def encrypt(self, k):
        plaintext = self.message
        ciphertext = ''
        for i in range(len(plaintext)):
            p = plaintext[i].upper()
            if p in self.alphabet:
                # index of shifted letter within alphabet
                x = (k + self.alphabet.index(p)) % 26
                # map this shifted index to a cipher
                c = self.alphabet[x % 26]
            else:
                # not encrypted as not in alphabet
                c = p
            # append each encrypted character to cipher string
            ciphertext += c
        return ciphertext

    def decrypt(self, k):
        ciphertext = self.message
        plaintext = ''
        for i in range(len(ciphertext)):
            c = ciphertext[i]
            if c in self.alphabet:
                x = (self.alphabet.index(c) - k) % 26
                p = self.alphabet[x % 26]
            else:
                p = c
            plaintext += p
        return plaintext.upper()


if __name__ == '__main__':
    while True:
        message = input('Enter path to file or (q) to quit: ')
        alphabet = input('Enter path to alphabet or (q) to quit: ')
        if message in 'qQ' or alphabet in 'qQ':
            break
        caesar = CaesarCipher(m=message, a=alphabet)
        if caesar:
            while True:
                menu = input('Caesar Cipher\n'
                             '(B)rute force key\n'
                             '(E)ncrypt message\n'
                             '(D)ecrypt message\n\n'
                             'Enter your choice (B/E/D): ')
                if menu in 'bB':
                    key = caesar.brute_force_key()
                    print(f'You found the key value of {key}')
                elif menu in 'eE':
                    key = int(input('Enter your encryption key: '))
                    caesar.encrypt(k=key)
                elif menu in 'dD':
                    key = int(input('Enter the decryption key: '))
                    caesar.decrypt(k=key)
                elif menu in 'qQ':
                    break
