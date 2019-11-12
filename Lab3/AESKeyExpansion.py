#!/usr/bin/python3

from AES import sbox, rcon

""" XOR Method for two hexdecimal parameters """
def xor(a, b):
    # cast hex char as integer to perform xor operation, return hex result and slice '0x' from string
    return hex(int(a, base=16) ^ int(b, base=16))[2:]

""" Shift the row of the word matrix """
def shift_rows(word):
    word_length = int(len(word)/4)
    splitword = [word[i: i + word_length] for i in range(0, len(word), word_length)]
    rotword = splitword[1] + splitword[2] + splitword[3] + splitword[0]

    #return rotated word where each hex value has been sepreated, i.e '0f1571c9' becomes ['0f', '15', '71', 'c9']
    return [rotword[i: i + word_length] for i in range(0, len(rotword), word_length)]

""" Substitute all the words with the corresponding sbox value by using the index of word in lookup table """
def sub_bytes(word):
    #here we left shift the word by 1 place
    rotword = shift_rows(word)
    sub_word = []
    #loop takes the rotated word, takes each value and uses it as coordinates to find new value in the sbox
    for i in range(4):
        # convert rotword to list to lookup sbox table by row and col, eg. ['0', 'f'] is row 0 col 15
        index = list(rotword[i])
        # exchange the hex value with the corresponding value from sbox table and append it to new list
        sub_word.append(sbox[int(index[0], base=16)][int(index[1], base=16)])

    return sub_word[0] + sub_word[1] + sub_word[2] + sub_word[3]


if __name__ == '__main__':
    # Initialising the given key
    key = '0f1571c947d9e8590cb7add6af7f6798'
    print(f'Given key: {key}')
    # creating empty list of 44 words to be popualted later
    words = [0] * 44

    # get the length of a word from a key
    word_length = len(key) // 4
    # using list comprehension to parse the key into 4 words from the provided key
    words = [key[i: i + word_length] for i in range(0, len(key), word_length)]

    # Expansion key loop, iterate and create words from given key
    for i in range(4, 44):
        temp = words[i - 1]
        # check for every 4th word pass to the g function
        if i % 4 == 0 :
            #the word is left shifted and substituted with sbox
            subword = sub_bytes(temp)
            #xor the sbox word with constant rcon add padding to string
            temp = xor(subword, rcon[(i // 4) -1] + '000000')

        # xor with previous word and appended to the words array
        words.append(xor(words[i - 4], temp))

    # output all the expanded keys from the algorithm
    for i in range(len(words)):
        print(f'Word[{i}]: {words[i]}')
