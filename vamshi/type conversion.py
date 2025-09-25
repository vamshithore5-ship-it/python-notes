#type conversion in python
#list to tuple
my_list = [1234]
my_tuple = (my_list)
print(my_list)
print(tuple(my_list))
print(my_tuple)

#tuple to list
my_tuple =(5,6,7,8,)
my_list =list(my_tuple)
print(my_list)
print(type(my_list))

#list to set
my_list = [1,2,2,3,3,4]
my_set = set(my_list)
print(my_list)
print(type(my_set))

#set to list
my_set={10,20,30}
my_list=list(my_list)
print(my_list)

#dictionary to list of keys
student = {"name": "john", "age": 20, "grade": "a"}
keys_list = list(student.keys())
values_list = list(student.values())
print(values_list)

#dictionary to list of items
student = {"name": "john", "age": 20,}
items_list = list(student.items())
print(items_list)

