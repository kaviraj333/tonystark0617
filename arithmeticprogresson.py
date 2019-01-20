N=int(input())
A=int(input())
D=int(input())
sum = 0
e = (N * D)
if (1<=e<=100000):
    if (1 <=A<= 100000):
        if (1 <=D<= 100000):
            for i in range (A,e+1,D):
                sum=sum+i
            print(sum)
