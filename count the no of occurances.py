#inp=input("give list: ").split(',')

#l=[int(a) for a in inp]
# sample input = [1,2,3,4,5,3,2,5,4]

l=[int(a) for a in input().split(',')]
b=int(input( "enter a specific number to count: "))
count=0
for i in l:
    if i == b:
        count+=1
    else:
        continue
print(f"count of {b}={count}")