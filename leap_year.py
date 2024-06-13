s=int(input("enter a year:"))
if (s % 4 ==0) and (s%100 !=0):
    print("it is a leap year")
elif (s%100==0 and s%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")