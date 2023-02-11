x=[2,7,4,89,36,8,3,2]
num=0
asc=False
for i in x:
    if num<i:
        num=i
        asc=True
    else:
        asc=False
        break
if asc:
        print("Not is Asscending order")
else:
        print("descending")