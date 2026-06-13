print('THIS IS A CALCULATOR !')
num1=int(input('ENTER THE FIRST NUMBER: '))
num2=int(input('ENTER THE SECOND NUMBER: '))
print('''TYPE THE NUMBER NEXT TO THE ACTION YOU WANT TO PERFORM
ADDITION ----------> 1
SUBTRACTION -------> 2
MULTIPLICATION ----> 3
DIVISION ----------> 4''')
act=int(input())
if act==1:
    print('{} + {} = {}'.format(num1,num2,num1+num2))
elif act==2:
    print('{} - {} = {}'.format(num1,num2,num1-num2))
elif act==3:
    print('{} * {} = {}'.format(num1,num2,num1*num2))
elif act==4:
    print('{} / {} = {}'.format(num1,num2,num1/num2))
else:
    print('PLEASE ENTER THE OPTIONS GIVEN')