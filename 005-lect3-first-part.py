##lect 3 task 1
print ('##lect 3 task 1')
y= input ('input number of month:')
y=int(y)
#fuction season
def season(x):
    if (x in (12,1,2)):
        ses='wither'
    elif (x in (3,4,5)):
        ses='sprint'
    elif (x in (6,7,8)):
        ses='summer'
    elif (x in (9,10,11)):
        ses='authumn'

    return ses

print (season(y))

##lect 3 task 2
print ('##lect 3 task 2')
y= input ('input number for check:')
y=int(y)

#fuction isPrime
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
if y in range(1 , 1000):
    z=isPrime(y)
    print(y, 'is prime number :', z)
else:
    print ('error input')



##lect 3 task 3

print ('##lect 3 task 3')
a= input ('input a :')
b =input ('input b :')
c =input ('input operation :')

#fuction arithmetic
def arithmetic(a,b,c):
    a=int(a)
    b=int(b)
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        return a / b
    elif c == '*':
        return a * b
    else:
        return 'unknown operation'


z=arithmetic(a,b,c)
print (z)

