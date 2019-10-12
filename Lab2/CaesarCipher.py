import os


class CaesarCipher:
    def __init__(self):
        while True:
            try:
                self.file_path = 'data/plaintext/message.txt'
                # self.file_path = self.get_file()
                with open(self.file_path) as file:
                    self.file = file.read()
                    filename = os.path.basename(self.file_path)
                    print(f'{filename} was found!')
                    break
            except OSError as e:
                print(e)
        while True:
            try:
                self.alphabet_path = 'data/alphabet/english.txt'
                with open(self.alphabet_path) as alphabet:
                    self.alphabet = alphabet.read()
                    filename = os.path.basename(self.alphabet_path)
                    print(f'{filename} was found!')
                    break
            except OSError as e:
                print(e)

        # self.key = self.brute_force_key(self.file.upper())
        self.ciphertext = self.encrypt(4, self.file)
        self.plaintext = self.decrypt(4, self.file)
        print(self.ciphertext)
        print(self.plaintext)


    def get_data(self):
        pass

    def brute_force_key(self, ciphertext):
        print(f'\n\t\t {ciphertext} KEY')
        for key in range(len(self.alphabet)):
            translated = ''
            for c in ciphertext:
                if c.isalpha():
                    num = self.alphabet.find(c)
                    num = num - key
                    if num < 0:
                        num = num + len(self.alphabet)
                    translated = translated + self.alphabet[num]
                else:
                    translated = translated + c
            print(f'\t{key} \t {translated}', end='')
        key = int(input('\nEnter the key: '))
        return key

    def encrypt(self, key, plaintext):
        ciphertext = ''
        for i in range(len(plaintext)):
            p = plaintext[i].upper()
            if p in self.alphabet:
                # index of shifted letter within alphabet
                x = (key + self.alphabet.index(p)) % 26
                # map this shifted index to a cipher
                c = self.alphabet[x % 26]
            else:
                # not encrypted as not in alphabet
                c = p
            # append each encrypted character to cipher string
            ciphertext += c
        return ciphertext

    def decrypt(self, key, ciphertext):
        plaintext = ''
        for i in range(len(ciphertext)):
            c = ciphertext[i]
            if c in self.alphabet:
                x = (self.alphabet.index(c) - key) % 26
                p = self.alphabet[x % 26]
            else:
                p = c
            plaintext += p
        return plaintext.upper()


if __name__ == '__main__':
    caesar = CaesarCipher()
