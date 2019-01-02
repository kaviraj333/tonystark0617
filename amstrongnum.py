num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   b = temp % 10
   sum += b ** 3
   temp //= 10
if num == sum:
   print("yes")
else:
   print("no")
