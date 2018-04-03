a = [22,0, 33,77,66,88,99,100]

#function sum all even  elements in  array
def sum_p(x):
    summa=0
    for i in x:
        if i%2==0 and i!=0:
               summa+=i
    return summa
#check sum fuction
z=sum_p(a)
print (z)

#fuction max in array
def max_p(x):
    result=0
    for i in x:
        if i>result:
            result=i
    return result
#check fuction
m=max_p(a)
print (m)
##fuction min in array
def min_p(x):
    result=0
    for i in x:
        if i<result:
            result=i
    return result
#check fuction min
mi=min_p(a)
print (mi)
#fuction summ all from array
def sum_all(x):
    summ=0
    for i in x:
        summ+=i
    return summ

print(sum_all(a))

#fuction sort array
def sortp(x):
    for i in range(0,len(x)-1):
        d=x[i]
        f=x[i + 1]
        if d>f:
            x[i+1]=d
            x[i]=f
    return x

z=sortp(a)
print (z)


##fuction revers  array

def reverp(x):
    ss=[]
    for i in range(len(x)-1,-1,-1):
        ss.append(int(x[i]))
    return ss
zz=reverp(a)
print(zz)


