def arm(N):
    sum = 0
    temp = N
    while temp >0 :
        b = temp % 10
        sum += b ** 3
        temp //= 10
    if N == sum:
        return True
    else:
        return False

for i in range(1,10000,1):
    if(arm(i)):
        print(i)
        
