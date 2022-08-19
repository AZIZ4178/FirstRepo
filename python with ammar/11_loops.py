x=0
while(x<5):
    print(x)
    x=x+1
for x in range(4,11):
 print(x)

days=["Mon","Tues","Wed","Thurs","Friday","Saturday","Sunday"]
for d in days:
    # if (d=="Friday"):break
    if (d=="Friday"):continue

    print(d)