from math import gcd


p = int(input("Enter P: "))
q = int(input("Enter S: "))
n = p * q
tn = (p - 1) * (q - 1)
e = 2
while gcd(e,tn) != 1:
    e += 1
d = 1
while (d * e) % tn != 1:
    d += 1
print(f"Public key: ({e},{n})")
print(f"Private key: ({d},{n})")
m = int(input("Enter the message: "))
c = pow(m,e,n)
print(f"Encrypted message: {c}")
m1 = pow(c,d,n)
print(f"Decrypted message: {m1}")
