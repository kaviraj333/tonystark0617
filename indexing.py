N=int(input())
test=[]
for i in range (1,N+1,1):
    a=int(input())
    test.append(a)
for i in range (0,len(test)):
    print(test[i],test.index(test[i]))
