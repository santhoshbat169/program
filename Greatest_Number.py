n1=int(input('ENTER THE FIRST NUMBER: '))
n2=int(input('ENTER THE SECOND NUMBER: '))
n3=int(input('ENTER THE THIRD NUMBER: '))
if n1>n2 and n1>n3:
    print('{a} is greatest among {a},{b},{c}'.format(a=n1,b=n2,c=n3))
elif n2>n1 and n2>n3:
    print('{b} is greatest among {a},{b},{c}'.format(a=n1,b=n2,c=n3))
else:
    print('{c} is greatest among {a},{b},{c}'.format(a=n1,b=n2,c=n3))