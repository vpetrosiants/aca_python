import datetime
now = datetime.datetime.now()
n_year = now.year
#get user name
name= input ('Please input your name:')
# test input  name , only letters
test_name = name.isdigit()

while (len(name)<=3 or test_name == True):
    #ask to try again
    n_check = input('Wrong input name, do you want retry?(y/n) :')
    if n_check == 'y':
        name = input('Please imput your name, again:')
        test_name=name.isdigit()
        if len(name)<=3:
            print ('name too short')
            name=''
        elif test_name == True:
            print('Name can\'t content digits')
            name=''
        else:
            pass
    else:
    #exit if 'No'
        print ('Goodbye!')
        break
# if len name more then 3 letters  and no digits
if (len(name)>3 and test_name==False):
    res = input ('Please input year:')
    test=res.isdigit() #test year for digits
    in_check=0 #flag for check
    while (len(res)<=3  or  test == False or len(res)>4 or (test ==True and int(res)>=n_year)): # if year < 3 digits or no digits or mor then 4 digits or ,ore then 2018
        in_check = input ('Wrong input, do you want retry1?(y/n) :')
        if in_check == 'y':
                res = input ('Please input year, again:')
                test=res.isdigit()
                if len(res)<=3:
                    print ('no values')
                    res=''
                elif len(res)>4:
                    print('year couldn\'t be in future')
                    res=''
                elif (test == True and int(res)>=n_year):
                    print('year couldn\'t be in future')
                    res = ''
                elif test == False:
                    print ('no number')
                    res=''
                else:
                    pass
        else:
          print('Goodbye!')
          in_check=''
          break
#if value of year is OK then continue

    if (in_check == 'y' or in_check==0):
        res=int(res)
        age = n_year - res
        if age < 18:
            print(name ,'Underage - Not permitted')
        elif age >=18:
            print ( name ,'Adult Club Memver')
    else:
        pass
else:
#    print('Goodbye!!')
    pass

















