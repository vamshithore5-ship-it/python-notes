num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Bitwise AND
bitwise_and = num1 & num2

# Bitwise OR
bitwise_or = num1 | num2

# Bitwise XOR
bitwise_xor = num1 ^ num2

# Bitwise NOT
bitwise_not_num1 = ~num1
bitwise_not_num2 = ~num2

# Bitwise left shift
bitwise_left_shift = num1 << 1

# Bitwise right shift
bitwise_right_shift = num1 >> 1

print(f"\n bitwise and of {num1} & {num2} = {bitwise_and}")
print(f"\n bitwise or of {num1} | {num2} = {bitwise_or}")
print(f"\n bitwise xor of {num1} | {num2} ^ {bitwise_xor}")
print(f"\n bitwise not of {num1} = {bitwise_not_num1}")
print(f"\n bitwise not of {num2} = {bitwise_not_num2}")
print(f"\n bitwise left shift of {num1} << 1 = {bitwise_left_shift}")
print(f"\n bitwise right shift of {num1} >> 2 = {bitwise_right_shift}")


