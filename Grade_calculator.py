m=int(input("enter marks in maths:"))
s=int(input("enter marks in science:"))
e=int(input("enter marks in english:"))
total=(m+s+e)
avg=(total/3)
# grade
grade=""
if avg >90 :
    grade=("A")
elif avg > 70 and avg <= 90:
    grade=("B")
elif avg > 50 and avg<=70:
    grade=("C")
else:
    grade=("fail")
print(f"Total_marks:{total}")
print(f"Average marks:{avg}")
print(f"Grade:{grade}")