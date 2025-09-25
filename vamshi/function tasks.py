#1)write a function mul_numbers(a,b) that returs the mul of a and b
def mul_numbers(a, b):
    return a * b
# Example usage:
a=int(input("enter a number for a"))
b=int(input("enter a number for b"))
result = mul_numbers(a, b)
print(result)

#2)the function should check if the number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Example usage:
print(check_even_odd(5))
print(check_even_odd(2))

#3)the function should return the factorial of n.
n1 = int(input("enter number"))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(n1))
    
#4)write a function largest_of_three(a,b,c)  
def largest_of_three(a, b, c):
    return max(a, b, c)
# Example usage:
a=int(input("enter a number for a"))
b=int(input("enter a number for b"))
c=int(input("enter a number for c"))
print(largest_of_three(a,b,c))

#5)reverse_string(s)
s = input("enter some strings")
def reverse_string(s):
    return(s[::-1])
print(reverse_string(str))

#6)function should return the number of vowels
word=input("enter your name")
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count+= 1
    return count
print(count_vowels(word))      