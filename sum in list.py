# for loop in
l=[10,20,30,40,50]
sum=0
for i in l:
    sum+=i
print(f"sum of elements:{sum}")
    
    
# by using range
l=[10,20,30,40,50]
sum=0
for i in range(5):
    sum+=l[i]
print(f"sum of elements:{sum}")

#by using while
l=[10,20,30,40,50]
sum=0
i=0
length=len(l)
while i < length:
    
    sum+=l[i]
    i+=1
print(f"sum of elements:{sum}")