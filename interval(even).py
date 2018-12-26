a=int(input())
b=int(input())
for i in range (a,b,1):
    q=i%2
    if q==0:
        print(i)
print(q)
