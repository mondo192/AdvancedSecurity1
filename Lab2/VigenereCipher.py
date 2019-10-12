import os


class VigenereCipher:
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

        self.ciphertext = self.encrypt('4', self.file)
        # self.plaintext = self.decrypt(4, self.file)
        print(self.ciphertext)
        # print(self.plaintext)

    def encrypt(self, key, plaintext):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    def decrypt(self, key, ciphertext):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext


if __name__ == '__main__':
    app = VigenereCipher()