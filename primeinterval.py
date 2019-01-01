N=int(input())
K=int(input())
for c in range (N,K+1):

    if (c>1):
        for i in range (2,c):

            if(c%i)==0:
                break
        else:
                print(c)

