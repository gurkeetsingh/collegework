print("the program to add the number")
num=int(input("enter the number"))
add=0
while(num>0):
    add=add+(num%10)
    num=num//10

print(add)