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
