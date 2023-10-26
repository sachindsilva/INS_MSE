import numpy as np


l = list(map(int, input("Enter the key matrix : ").split()))
keyMatrix = np.array(l).reshape(2, 2)
det = keyMatrix[0, 0]*keyMatrix[1, 1]-keyMatrix[1, 0]*keyMatrix[0, 1]

det = pow(int(det), 1, 26)
detInverse = pow(det, -1, 26)

keyInverse = np.array([[keyMatrix[1, 1], -keyMatrix[0, 1]],
                      [-keyMatrix[1, 0], keyMatrix[0, 0]]])

keyInverse = (keyInverse*detInverse) % 26


def text_to_num(text):
    return [ord(char)-ord('A') for char in text]


def num_to_text(nums):
    return "".join([chr(num+ord('A')) for num in nums])


def encrypt(plainText):
    plainText= plainText.upper().replace(' ','')
    if(len(plainText)%2!=0):
        plainText+="X"

    cipherText = ""
    
    for i in range(0,len(plainText),2):
        block = np.array(text_to_num(plainText[i:i+2]))
        encrypted_block = np.dot(keyMatrix,block)%26
        cipherText+=num_to_text(encrypted_block)
    return cipherText

def decrypt(cipherText):
    cipherText = cipherText.upper().replace(' ','')
    plainText = ""

    
    for i in range(0,len(cipherText),2):
        block = np.array(text_to_num(cipherText[i:i+2]))
        decrypted_block = np.dot(keyInverse,block)%26
        plainText+=num_to_text(decrypted_block)
    return plainText


plainText = input("Enter a message :")

cipherText = encrypt(plainText)
print("Encrypted : ",cipherText)


print("Decrypted : ",decrypt(cipherText))



    