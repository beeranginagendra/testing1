n=int(input( "enter the number to get factorial:"))
fact=1
if n==0 or n==1:
    print('factorial of ',n,'is 1')
else:
    while n>1:
        fact=fact*n
        n=n-1
print(fact)
