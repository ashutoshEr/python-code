
year1 = int(input('enter year 1 : '))

year2 = int(input('enter year 2 : '))

if(year1%4==0 and year1%100!=0 or year1%400==0):
            print(year1, 'is leap year')
               
else:
            print(year1, 'is not leap year')

if(year2%4==0 and year2%100!=0 or year2%400==0):
                print(year2, 'is leap year')
else:
                print(year2, " is'nt leap year")           