n=int(input("enter n value"))
i=1
while i<=n:
    if not i%2==0:
        i+=1
        continue
        
    print("even:",(i))
    i+=1