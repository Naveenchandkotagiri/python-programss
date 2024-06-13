temp=int(input("enter temperature:"))
cen=input("enter units k or f or c:")

a=cen.lower()
if a=="c":
    print(f"temperature in farenheat:{temp*(9/5)+32}")
    print(f"temperature in kelvin:{273+temp}")
elif a=="f":
    print(f"temperature in degree celcius:{(temp-32)*5/9}")
    print(f"temperature in kelvin:{(temp-32)*5/9+273.15}")
elif a=="k":
     print(f"temperature in farenheat:{(temp-273.15)*9/5+32}")
     print(f"temperature in centigrade:{temp-273.15}")
else:
    print(f"enter valid input:")