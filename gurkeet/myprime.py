from ast import Num


n=int(input("enter the number"))
#flag=False
for n in range(3,n):
    for i in range(2,n):
        if(n%i==0):
            #flag = True
            break
    else:
        print(n)
    '''if flag == True:
        print("number is not prime")
    else:
        print("your number is prime")'''
