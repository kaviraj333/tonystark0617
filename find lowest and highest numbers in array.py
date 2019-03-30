a=int(input())
c=[]
if (a<=10000):
    for i in range (a):
        b=int(input())
        c.append(b)
    print(min(c),max(c),end=' ')    
    
