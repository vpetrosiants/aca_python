import datetime
now = datetime.datetime.now()
n_year = now.year
res = input ('Please input year:')
test=res.isdigit()

while (len(res)<=0  or  test == False):
    in_check = input ('Wrong input, do you want retry?(y/n) :')
    if in_check == 'y':
            res = input ('Please input year, again:')
            test=res.isdigit()
            if len(res)<=0:
                print ('no values')
                res=''
            elif test == False:
                print ('no number')
                res=''

            else:
                pass
    else:
      print('Goodbye!')
      break

res=int(res)
age = n_year - res
if age < 18:
    print('Underage')
elif age >=18:
    print ('Adult')
