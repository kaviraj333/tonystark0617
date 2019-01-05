def fact(a):
    if a==1:
        return a
    else:
        a=a*fact(a-1)
        print(a)
        return a
x=int(input())
b=fact(x)
print(b)
