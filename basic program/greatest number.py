a=int(input("Please Enter a Number : "))
if(a&1==1):  
    print("This Number is Odd")    
else:  
    print("This Number is Even")
     

for i in range(1,101):
     if i%3==0 or i%5==0:
         continue
     print(i)