N=int(input())
if (1<=N<=100000):
    list1=[]
    for i in range (1,N+1,1):
        c=int(input("enter : "))
        list1.append(c)
    print(max(list1))
    
