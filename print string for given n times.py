a=input()
digit=""
str=""
for i in range(len(a)):
    if (a[i].isdigit()):
        digit=a[i]+digit
    else:
        str=str+a[i]
for i in range(int(digit)):

    print(str)
        
