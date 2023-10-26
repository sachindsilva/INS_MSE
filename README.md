# INS_MSE


**1,CAESAR CIPHER**

```py


def encrypt(text,s):
    result=""
    
    for i in range(len(text)):
        char = text[i]
        
        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        elif(char.islower()):
            result+=chr((ord(char)+s-97)%26+97)
        else:
            result+=" "
            
    return result


def decrypt(text,s):
    result=""
    
    for i in range(len(text)):
        char = text[i]
        
        if(char.isupper()):
            result+=chr((ord(char)-s-65)%26+65)
        elif(char.islower()):
            result+=chr((ord(char)-s-97)%26+97)
        else:
            result+=" "
            
    return result



while True:
    text=input("Enter a text : ")
    key = int(input("Enter a key : "))
    choice = int(input("1.Encryption\n2.Decryption\n3.Exit\nEnter a choice : "))
    
    if(choice == 1):
        print("The cipher text : "+encrypt(text,key))
    elif(choice == 2):
        print("The plain text : "+decrypt(text,key))
    elif(choice == 3):
        break
    else:
        print("Please enter the correct number")
```

---

**2.MONOALPHABETIC CIPHER**

```py


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
```


**3.DIFFIE-HELMAN CIPHER**

```py


q = int(input("Enter a prime number : "))
a = int(input("Enter a primitive root : "))

Xa = int(input("Enter private key of A :"))
Xb = int(input("Enter private key of B :"))


Ya = pow(a,Xa)%q
Yb = pow(a,Xb)%q


print("Public key of A : ",Ya)
print("Public key of B : ",Yb)

Ka = pow(Ya,Xb)%q
Kb = pow(Yb,Xa)%q

print("Shared key of A : ",Ka)
print("Shared key of B : ",Kb)
```
---

**4.VIGNERE CIPHER**


```py


def vigenere(key,message):
    message = message.lower()
    message=message.replace(' ','')

    m =len(key)
    cipherText = ""

    
    for i in range(len(message)):
        letter = message[i]
        k = key[i%m]
        cipherText = cipherText+chr((ord(letter)+k-97)%26+97)

    return cipherText


if __name__ == "__main__":
    print("Encrypting..")
    key = input("Enter keystream : ")
    key = [ord(letter)-97 for letter in key]

    message = input("Enter a message :")
    cipherText = vigenere(key,message)
    print("Cipher text : ",cipherText)

    print("Decrypting ..")
    key = [-1*k for k in key]
    plainText = vigenere(key,cipherText)
    print("Plain text : ",plainText)
    
```

---

**5.RSA**

```py
import math

def gcd(a,b):
    temp = 0
    
    while(1):
        temp = a %b
        if(temp == 0):
            return b
        a = b
        b = temp

    
p = 3
q = 7
n = p*q
e=2

phi = (p-1)*(q-1)

while(e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e=e+1
        
        
k=2
d=(1+(k*phi))/e
message = 12.0

print("Message data = ",message)
c=pow(message,e)
c = math.fmod(c,n)
print("Encrypted data = ",c)
m = pow(c,d)
m=math.fmod(m,n)
print("Original message : ",m)

```

---


**6.HILL CIPHER**

```py
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
```

---

**7.FIESTEL**

```py
# Fiestel cipher


s = input("Enter a string : ")


# This will convert string to ASCII--> then to 8-bit binary
result = "".join(format(ord(i),'08b') for i in s)


print("Result : ",result)

l = int(len(result)/2)

left = result[:l]
right = result[l:]


k = input("Enter a key : ")
key = "".join(format(ord(i),'08b') for i in k)
s = bin(int(right,2)+int(key,2))
answer = bin(int(s[2:],2)^int(left,2))

newr= answer[2:]
newl = right


newr,newl = newl,newr

s= bin(int(newr,2)+int(key,2))
ans = bin(int(s[2:],2) ^ int(newl,2))
nl = newr

nr = ans[2:]
nl,nr = nr,nl
cipher = nl+nr

if(len(cipher)!=len(result)):
    while(len(cipher)!=len(result)):
        cipher="0"+cipher

print(cipher)

plainText = ""
for i in range(0,len(cipher),8):
    temp = cipher[i:i+8]
    d = int(temp,2)
    plainText=plainText+chr(d)
    
print(plainText)
```

---

**8**

###### _will be updated_


---