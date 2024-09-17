print "Enter first number"
x = input()
print "Enter second number"
y = input()
#x,y = 10, 20 means x = 10 y = 20
while y != 0:
  x, y = y, x % y
print x
