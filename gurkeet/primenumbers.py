print("program to find a prime numbers")
num=int(input("enter the numbers between which you want to find prime nums:"))
for num in range(1,num+1):
   if  num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
    