#introduction of collection data types:
#COLLECTION DATA TYPES:are used to store multiple values in a single variable.
#there are four types of collection data types
#1.list A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [].
#example for list  
fruits = ['apple', 'banana', 'mango',]
print(fruits)
#adding an element
fruits.append('orange')
print(fruits)
#removing an element
fruits.remove('banana')
print(fruits)
#changing an element in a list
fruits[1] = 'grapes'
print(fruits)
#acess elements from a list
fruits=['apple', 'banana', 'mango', 'grapes', 'orange',]
print(fruits[0]) #first fruit
print(fruits[-1]) #last fruit
#sort the list
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)#output: [1, 2, 5, 7, 9]