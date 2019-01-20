N=int(input())
if (1<=N<=1000):
    list1=[]
    for i in range (1,N+1,1):
        c=int(input("enter : "))
        list1.append(c)
    print(list1)
    list1.sort()
    print(list1)


