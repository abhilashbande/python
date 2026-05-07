list = [1,2,3,4,5,6];

print(type(list))

# accessing

print(list[0])
print(list[-len(list)])
print(list[-1])

# mutability
print("id = ", id(list))
list[2] = 10
print("id = ", id(list))
print(list)

# iterable

for i in list:
    print(i, end=", ")

print("\n")

# slicing
print(list[0:3])