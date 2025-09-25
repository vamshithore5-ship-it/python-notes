78#explain datatypes and variables with examples

# data types are used to store different types of values in programming,by using this we can execute programs
# variables are used to store data values.
#x=10 #x is an variable & 10 is an integer data type
#y=3.12 #y is a variable & 3.12 is a float data type
#print(x+y)

# Examples of data types:
# 1. Integer: whole numbers (ex., 5, -10, 0)
# 2. Float: decimal numbers (ex., 3.14, -0.001)
# 3. String: text (ex., "Hello World",)
# 4. Boolean: True or False values (ex., True, False)


# Examples of variables:
# 1. age = 25 (integer variable)
# 3. name = vamshi (string variable)

#explain about conditional statements along with examples
# conditional statement is used to whether the condition is true are false ,
#there are three tyoes of conditional statements
# 1.if statement
# 2.if else statement
# 3.if elif else statement

#example for if statement
#num = int(input("enter your marks: "))
#if num > 90:
 #   print("you got A grade")

#example for if else statement
#num = int(input("enter your marks: "))    
#if num >= 50:
#    print("your passed")
#else:
 #   print("your failed")

#example for if elif else statement
#num = int(input("enter your weight: "))
#if num < 50:
#    print("you are underweight")
#elif num >= 50 and num < 100:
#    print("you are normal weight")
#else:
#    print("you are overweight")
#
#num=int(input("enter your age: "))
#if num < 18:
#    print("you are NOT ELGIBLE to vote")
#else:
#     print("you are ELGIBLE to vote")

#prime numbers between 100 and 500
#start = 100
#end = 500
#num = start
#while num <= end:
#    is_prime = True
#    if num < 2:
#        is_prime = False
#    else:
#        i = 2
#        while i * i <= num:
#            if num % i == 0:
#                is_prime = False
#                break
#           i += 1
#    if is_prime:
#        print(num)
#    num += 1

#num=13
#print(f"multiplication table for {num}")
#for i in range(1,11):
#    print(f"{num} x {i} = {num*i}")

#calculate the sum of first five natural numbers
#sum = 0
#for i in range(1, 6):
#    sum += i
#print(f"The sum of the first five natural numbers is: {sum}")


#print square of numbers from 1 to 5

#num=int(input("enter a number: "))
#if num%2==0 and num>=0:
#        print(f"{num} is even number and positive number")
#elif num%2==0 and num<0:
#        print(f"{num} is even number and negative number")
#elif num%2!=0 and num>0:
#        print(f"{num} is odd number and positive number")
#elif num%2!=0 and num<0:
#        print(f"{num} is odd number and negative number")


username = input("enter username: ")
if username == "thevamshu":
    password = input("enter password: ")
    if password == "770226":
        print("Login successful!")
    else:
        print("Invalid password.")
else:
    print("Invalid username.") 
