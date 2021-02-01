
def check(year):
        

        if(year%4==0 and year%100!=0 or year%400==0):
                print(year, 'is leap year')
                
        else:
                print(year, 'is not leap year')

year1 = int(input('enter year1: '))
year2 = int(input('enter year2: '))
check(year1)
check(year2)