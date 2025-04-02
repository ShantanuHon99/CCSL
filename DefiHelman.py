n=int(input("Enter N (Prime) : "))
g=int(input("Enter G (Prime) : "))

primitive=[]
for i in range(1,g):
    rem=pow(n,i)%g
    primitive.append(rem)
    if(primitive.count(rem)>1):
        print("Not Primitive. Execution Terminated")
        exit()
a_pvt=int(input("Input Private Key for A : "))
b_pvt=int(input("Input Private Key for B : "))
A=pow(g,a_pvt,n)
print(f"Private Value of A: {A}")
B=pow(g,b_pvt,n)
print(f"Private Value of A: {B}")
Key_A=pow(B,a_pvt,n)
print(f"Key of A : {Key_A}")
Key_B=pow(A,b_pvt,n)
print(f"Key of B : {Key_B}")
if(Key_A==Key_B):
    print("Connection Successfully Established !!")