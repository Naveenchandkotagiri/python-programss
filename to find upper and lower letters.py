inp=input("enter some text")
a=0
b=0
for i in inp:
    if i.isupper():
        a+=1
    elif i.islower():
        b+=1
    else:
        pass
print(f"upper{a}")
print(f"lower{b}")
        