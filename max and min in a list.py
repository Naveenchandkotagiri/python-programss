l=[15,2,7,25,10]
a=l.sort()
print(f"max={l[-1]} min={l[0]}")

# by using loops
l=[15,2,7,25,10]
max=15
min=15
for i in l:
    if i > max:
        max=i
    if i< min:
        min=i
print(f"max = {max}\nmin={min}") 

      
         