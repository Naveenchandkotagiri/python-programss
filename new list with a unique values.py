# [10,20,30,20,40,10,50]
'''inp=input("enter values:").split(",")
l=[int(a) for a in inp]
s=set(l)
b=list(s)
b.sort()
print(b)
'''

# [10,20,30,20,40,10,50]
'''inp=input("enter values:").split(",")
l=[int(a) for a in inp]
newlist=[]
for i in l:
    if i in newlist:
        continue
    else:
        newlist.append(i)
print(newlist)'''


l=[10,20,20,30,40,30,50]
newlist=[]
newlist=[]
for i in l:
    if i in newlist:
        continue
    else:
        newlist.append(i)
print(newlist)