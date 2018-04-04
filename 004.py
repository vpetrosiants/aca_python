a= '  , first string and end of example'
b = '....  ..  second string number 2 and etc'

# delete all space in the begin of the string
a_d = a.lstrip(' ')
b_d = b.lstrip(' ')
print(a_d)

#delete all symbolds in the begining of the string
for i in a:
    if not i.isalpha() and i != ' ':
            a = a.replace(i, '')
# delete all space in the begin of the string
a_d = a.lstrip(' ')
# delet first letter in the string
a_d= a_d[1:]


#delete all symbolds in the begining of the string
for i in b:
    if not i.isalpha() and i != ' ':
            b = b.replace(i, '')
# delete all space in the begin of the string
b_d = b.lstrip(' ')
# delet first letter in the string
b_d= b_d[1:]


# make result
result=a_d + ' ' + b_d
print('task 1 :',result)

###### second tast

aa= '... , task two result new string .. '

#delete all symbolds in the string
for i in aa:
    if not i.isalpha() and i != ' ':
            aa = aa.replace(i, '')

#delete all spaces in the beginnind
b_d = aa.lstrip(' ')
#delete all spaces in the end
b_d = b_d.rstrip(' ')
#get 2 letters from the  end of the string
ress=b_d[-2:]
#new string for result
ress = ress*3
print('task 2 :',ress)


###### third task
xx = [5,2,9]

#fuction revers sort without reverse
def revers_sort(x):
    z=[]
    lenn=len(x)
    for i in range(0, lenn):
        mm=max(x)
        z.append(mm)
        x.remove(mm)
    return z
print ('task 3 :', 'input =', xx )
zz=revers_sort(xx)
print ('task 3 :', 'output -' ,zz)

###### fourth task
xx = [5,2,9]
def result_4(x):
    z=[]
    mm=max(x)
    z.append(mm)
    z.append(x)
    return z

print ('task 4 :',result_4(xx))

####fifth task

kk = [4,19,16,110,13,19,15,100]

#fuction sum of array exclude 13,14,17,18,19
def result_5(x):
    z = []
    summ_5=0
    for i in range(0, len(x)):
        j = x[i]
        if (j in range(12,14)) or (j in range(17,20)):
            j=0
        summ_5+=j
    return summ_5

print ('task 5 :','input -', kk ,'result :',result_5(kk))




