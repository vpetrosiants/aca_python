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



