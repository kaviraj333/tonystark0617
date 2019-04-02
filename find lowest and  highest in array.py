a=int(input())
c=list(map(int,input().split()))
b=[]
for i in range(a):
    b.append(c[i])
print(min(b),max(b),end=' ')    
