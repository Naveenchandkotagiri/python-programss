'''n=int(input("enter table number:"))
fact=1
while n>=1:
    fact*=n
    n-=1
print(fact)
'''
    # for loop
n=int(input("enter table number:"))
fact=1
for i in range (1,n+1) :
    fact=fact*i
print(fact)
