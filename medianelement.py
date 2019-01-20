N=int(input())
if (1<=N<=1000):
    list1=[]
    for i in range (1,N+1,1):
        c=int(input())
        list1.append(c)
    list1.sort()
    d=int(N/2)
    print(list1[d])


