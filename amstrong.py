N = int(input("Enter a number: "))
if (N<=100000):
    sum = 0
    temp = N
    while temp >0 :
        b = temp % 10
        sum += b ** 3
        temp //= 10
    if N == sum:
        print("yes")
    else:
        print("no")
else:
    print("invalid")
