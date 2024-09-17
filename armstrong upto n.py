num1= input('enter number loweer :')
num2= input('enter number upper:')
for i in range(num1,num2):
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if sum==i:
        print i 


#0, 1, 153, 370, 371, 407
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if sum==num:
#     print 'given number is arm strong'
# else:
#     print'given num is not arm strong'