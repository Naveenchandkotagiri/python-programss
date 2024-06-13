'''
n=int(input("enter n natural numbers:"))
sum=0
for i in range(1,n+1):
    sum=i+sum
print(sum)
'''

    # while loop

n=int(input("enter natural num:"))
sum=0
i=0
while i<=n:
    sum+=i
    i+=1
print(sum)