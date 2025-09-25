#print all prime numbers 
num=int(input("enter a number: "))
count=0
for i in range(1, num+1):
    if(num % i==0):
        count+=1
if(count==2):
    print("is a prime number")
else:
    print("is not a prime number")