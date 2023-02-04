x = int(input("enter first number for swapping"))
y = int(input("enter second number for swapping"))

def swapping(x,y):
    temp=x
    x=y
    y=temp
    print("first number after swapping",x)
    print("first number after swapping",y)
    swapping(x,y)
