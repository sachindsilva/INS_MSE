

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
