N=int(input())
K=int(input())
li=[]
for c in range (1,N+1,1):
    li.append(c)
print(li)
sum=0
for i in range (K):
    sum=sum+li[i]
print(sum)


