a= (input()).split(" ")
sum=0
if (len(a)<=1000):
    for x in a:
        sum=sum+len(x)
    print(sum)
