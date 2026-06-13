mark=int(input('ENTER THE MARK YOU GOT'))
if mark>80:
    print("YOUR GRADE IS 'A'")
elif mark>60 and mark<=80:
    print("YOUR GRADE IS 'B'")
elif mark>40 and mark<=60:
    print("YOUR GRADE IS 'c'")
else:
    print("YOU FAILED")