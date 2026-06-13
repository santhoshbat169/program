a=int(input())
if a%2==0 and a%3==0:
    print('{} is divisible by 2 and 3'.format(a))
elif a%2==0 and a%3!=0:
    print('{} is divisible by 2 but 3'.format(a))
elif a%2!=0 and a%3==0:
    print('{} is divisible by 3 but 2'.format(a))
else:
    print('{} is not divisible by both 3 and 2'.format(a))