'''s=input("enter some text:")
s1=s.lower()
a=s1.count('a')
e=s1.count('e')
i=s1.count('i')
o=s1.count('o')
u=s1.count('u')
print(f"Number of vowels:{a+e+i+o+u}")
'''







s=input("enter some text:")
vol='aeiouAEIOU'
y=[]
print(s)
for i in s:
    if i in vol:
        y.append(i)
print(y) 
a=y.count('a')
print(f"count of a:{a}")
e=y.count('e')
print(f"count of e:{e}")
i=y.count('i')
print(f"count of i:{i}")
o=y.count('o')
print(f"count of o:{o}")
u=y.count('u')
print(f"count of u:{u}")







