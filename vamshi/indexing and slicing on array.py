#1Q
import array
nums = array.array('i',[10,20,30,40,50])
print(nums[0])
print(nums[-1])
#2Q
import array
nums = array.array('i',[1,2,3,4,5])
print(nums[0:-1])
#3Q
import array
nums = array.array('i',[-1,-2,3,4,5,6,7,8,9,10,-3,-4])
positive_nums = [num for num in nums if num > 0]
print(positive_nums)
#4Q
import array
nums = array.array('i',[1,2,3,4,5])
print(nums[::2])
#5Q
import array
nums = array.array('i',[5,10,15,20,23,30])
sliced_array = nums[1:4]  # Example: slice from index 1 to 3
print(sliced_array)
totall=0
for num in sliced_array:
    totall =+num
    print(num)    

#6Q
import array
nums = array.array('i',[1,2,3,4,5])
reverse_array = nums[::-1]
print(reverse_array)