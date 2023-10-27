
import random

s = input("Enter a string : ")
result = "".join(format(ord(i),'08b') for i in s)

print("Result : ",result)


answer = ""

for i in range(len(result)):
    if(i%8!=0):
        answer+=result[i]


l = int(len(answer)/2)

left = answer[:l]
right=answer[l:]


lt = [2,3,6,7,1,6,5,9]
keys= []


for i in range(0,8):
    newKey = ""
    newAns = ""

    
    nl=int(left,2)
    nl=bin(nl<<lt[i])
    num=2+lt[i]
    
    nr=int(right,2)
    nr=bin(nr<<lt[i])
    num=2+lt[i]
    
    newKey = nr[num:]+nl[num:]
    rm = []
    
    
    while(len(rm)!=8):
        r = random.randint(0,len(newKey)-1)

        
        if(r not in rm):
            rm.append(r)

        
    for i in range(len(newKey)):
        if(i not in rm):
            newAns+=newKey[i]

    keys.append(newAns)


for i in range(0,len(keys)):
    print("Key ",i+1," : ",keys[i])
