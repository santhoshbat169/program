def sum(a,b):
    c=a+b
    print(c) #for printing this no return func is needed cuz' this is in the block and have nothing just print
    return c
x=int(input())
y=int(input())
print('value is',sum(x,y)) #but for this return is needed because the func is in print function like func in func.