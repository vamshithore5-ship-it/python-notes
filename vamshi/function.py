#syntax
def function_name():
    #code block
    print("hello.world!")
#example:
def greet():
    print("welcome to python functions!")
    greet()
#passing parameter & arguments example:
def greet_user(name):
    print("hello,", name)
#calling function with arguments
greet_user("hero")
#output:hello,hero
#functional arguments types:
#ex:
def add(a, b):
    print("sum is:", a + b)
add(5, 10)
#output:sum is:15
#keywoed argument
# specify argument by parameter name
def introduce(name,age):
    print(f"my name is{name} and iam {age} years old")  
    introduce(age=29,name="hero")
#default arguments
def greet(name="guest"):
    print("hello,", name)
    greet()#output:hello,ram
    greet("ram")#output:hello,ram

#higher order functions
#map()
def square(x):
    return x*x
number =[1,2,3,4,5]
squared = list (map(square,number))
print(squared)#output:[1,4,9,16,25]


#filter()
def is_even(x):
    return x% 2 ==0
numbers =[1,2,3,4,5,6]
even_numbers =list(filter(is_even,numbers)) 
print(even_numbers) #output[2,4,6] 

#reduce()
from functools import reduce
def add(x,y):
    returnx+ynumber = [1,2,3,4,5]
        
