def special(a):
    special=""
    num=""
    str=""
    for i in range(len(a)):
        if (a[i].isdigit()):
            num=num+a[i]
        elif((a[i] >= 'a' and a[i] <= 'z') or (a[i] >= 'A' and a[i] <= 'Z')):
            str=a[i]+str
        else:
            special=special+a[i]         
    print((len(special)-1))
r=input()
special(r)
