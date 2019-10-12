import os


class VigenereCipher:
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

    def encrypt(self, k):
        plaintext = self.message
        key_length = len(k)
        key_as_int = [ord(i) for i in k]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    def decrypt(self, k):
        ciphertext = self.message
        key_length = len(k)
        key_as_int = [ord(i) for i in k]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext


if __name__ == '__main__':
    while True:
        message = input('Enter path to file or (q) to quit: ')
        alphabet = input('Enter path to alphabet or (q) to quit: ')
        if message in 'qQ' or alphabet in 'qQ':
            break
        vigenere = VigenereCipher(m=message, a=alphabet)
        if vigenere:
            while True:
                menu = input('Vigenere Cipher\n'
                             '(E)ncrypt message\n'
                             '(D)ecrypt message\n'
                             '(Q)uit\n\n'
                             'Enter your choice (E/D/Q): ')
                if menu in 'eE':
                    key = input('Enter your encryption key: ')
                    ciphertext = vigenere.encrypt(k=key)
                    print(f'Ciphertext: {ciphertext}')
                elif menu in 'dD':
                    key = input('Enter the decryption key: ')
                    plaintext = vigenere.decrypt(k=key)
                    print(f'Plaintext: {plaintext}')
                elif menu in 'qQ':
                    break
