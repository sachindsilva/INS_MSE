

l = []


def encrypt(a, dict1):
    for x in a:
        y = dict1.get(x)
        l.append(y)
    return ''.join(l)


def decrypt(dict1):
    keyList = list(dict1.keys())
    valueList = list(dict1.values())

    print("Decrypted values are ")

    for i in l:
        position = valueList.index(i)
        print(keyList[position], end="")


dict2 = {'A': 'Z',
                'B': 'Y',
                'D': 'W',
                'C': 'X',
                'E': 'V',
                'F': 'U',
                'G': 'T',
                'H': 'S',
                'I': 'R',
                'J': 'Q',
                'K': 'P',
                'L': 'O',
                'M': 'N',
                'N': 'M',
                'O': 'L',
                'P': 'K',
                'Q': 'J',
                'R': 'I',
                'S': 'H',
                'T': 'G',
                'U': 'F',
                'V': 'E',
                'W': 'D',
                'X': 'C',
                'Y': 'B',
                'Z': 'A',
                'a': 'z',
                'b': 'y',
                'c': 'x',
                'd': 'w',
                'e': 'v',
                'f': 'u',
                'g': 't',
                'h': 's',
                'i': 'r',
                'j': 'q',
                'k': 'p',
                'l': 'o',
                'm': 'n',
                'n': 'm',
                'o': 'l',
                'p': 'k',
                'q': 'j',
                'r': 'i',
                's': 'h',
                't': 'g',
                'u': 'f',
                'v': 'e',
                'w': 'd',
                'x': 'c',
                'y': 'b',
                'z': 'a'
            }


x = input("Enter a message :")
encryption = encrypt(x, dict2)

print("Cipher text : ", encryption)
decryption = decrypt(dict2)
