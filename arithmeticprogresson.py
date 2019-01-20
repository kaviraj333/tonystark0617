N=int(input())
A=int(input())
D=int(input())
sum=0
e=(N*D)
for i in range (A,e+1,D):
    sum=sum+i
print(sum)
