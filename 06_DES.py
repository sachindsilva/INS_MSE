import random

s = input("Enter a string :")
result = "".join(format(ord(i),'08b') for i in s)

ans = ""

#Initial permutation

for i in range(len(result)):
    if(i%8!=0):
        ans+=result[i]

l=int(len(ans)/2)
left=ans[:l]
right=ans[l:]
lt=[2,3,6,7,1,6,5,9]
keys=[]
        
        