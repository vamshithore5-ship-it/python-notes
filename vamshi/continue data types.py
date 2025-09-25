#skip negative numbers
num=[12,-13,45,-4]
for num in num:
    if num<0:
        continue
    print(num)
#skip multiple numbers by 3
for i in range(1,30):
    if i%3 ==0:
        continue
    print(i)  