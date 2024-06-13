# basic calculator to perform +, -, /, * .
num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
operator=input("enter operator:")

if operator =="+":
    print(f"Addition:{num1+num2}")
elif operator == "-":
    print(f"Subtraction:{num1}-{num2}")
elif operator == "/" :
    print(f"Division:{num1/num2}")
elif operator == "*":
    print(f"Multiplication:{num1}*{num2}")
else:
    print("Enter correct operator")
    
    