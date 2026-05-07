# list = [1,2,3,4,5,6];

# print(type(list))

# # accessing

# print(list[0])
# print(list[-len(list)])
# print(list[-1])

# # mutability
# print("id = ", id(list))
# list[2] = 10
# print("id = ", id(list))
# print(list)

# # iterable

# for i in list:
#     print(i, end=", ")

# print("\n")

# # slicing
# print(list[0:3])


## List methods
# list = [100, 200, 100, 150, 250, 300, 100];

# print(list.count(100))
# print(list.index(250))  # if object is not in the list then it will throw an error

# print(list.pop())  # removes the last element
# print(list)

# list.remove(100) # removes the first occurrence of the element
# print(list)

# # list.remove(20); # if the element is not in the list then it will throw an error

# list.sort();
# print(list)

# list.insert(2, 500) # inserts 500 at index 2
# print(list)

# list.append(400) # adds 400 at the end of the list
# print(list)

# l1 = [111,222,333];
# list.append(l1) # adds the list l1 as a single element at the end of the list
# print(list)

# l1.extend(list);
# print(l1)


# hetrogeneous list
# list = [2, "Abhi", True, 3.14]

# for i in list:
#     print(type(i))


# 2-D List

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

list = [l1, l2, l3]
print(list)

for i in list:
    for j in i:
        print(j, end=" ")
    print()
