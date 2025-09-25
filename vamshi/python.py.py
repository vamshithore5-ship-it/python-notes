# example for data type
val1 = int(input("enter val1: "))
val2 = int(input("enter val2: "))
print('val1+val2=',val1+val2)  #addition
print('val1-val2=',val1-val2)  #subtraction

# example for string data type
# concatenation of two strings x=10
first_name=input("enter first name:")
last_name=input("enter last name:")
print("full name:",first_name+last_name)

# string repetition
print("repeated name:",first_name*3)

# string slicing
print("sliced name (first 2 chars):",first_name[:2])

# string length of string
print("length of string:", len(first_name))

#string conversion
print("string to upper case: ", first_name.upper())
print("string to lower case: ", first_name.lower())

#swap case
print("string swap case:", last_name.swapcase())

#control flow
age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")



































